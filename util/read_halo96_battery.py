# /// script
# requires-python = ">=3.10"
# dependencies = ["hidapi==0.15.0"]
# ///

"""Read one battery sample from the experimental Halo96 V2 firmware."""

import argparse
from time import monotonic

import hid


class BatteryFrame:
    def __init__(self):
        self.symbols = []
        self.started = 0.0
        self.charging = False

    def consume(self, report, now):
        if len(report) < 3 or report[0] != 0x03:
            return None

        usage = report[1] | (report[2] << 8)
        if usage == 0x0F:
            self.symbols = [usage]
            self.started = now
        elif usage == 0x07:
            self.charging = self.symbols == [0x0F] and now - self.started <= 0.5
            self.symbols = [usage]
            self.started = now
        elif not self.symbols or now - self.started > 0.5:
            self.symbols.clear()
        elif self.symbols == [0x07] and 0x08 <= usage <= 0x0E:
            self.symbols.append(usage)
        elif len(self.symbols) == 2 and 0x10 <= usage <= 0x1F:
            self.symbols.append(usage)
        elif len(self.symbols) == 3 and usage == 0:
            _, high, low = self.symbols
            self.symbols.clear()
            percent = ((high - 0x08) << 4) | (low - 0x10)
            return (percent, self.charging) if percent <= 100 else None
        else:
            self.symbols.clear()
        return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeout", type=int, default=25, help="seconds to wait for a complete frame")
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("--timeout must be positive")

    receivers = [
        device
        for device in hid.enumerate(0x19F5, 0x3247)
        if (device["usage_page"], device["usage"]) == (0x0C, 0x01)
        and device["product_string"] == "NuPhy Halo96 V2 Dongle"
    ]
    if len(receivers) != 1:
        parser.exit(1, "Connect exactly one NuPhy Halo96 V2 receiver.\n")

    frame = BatteryFrame()
    receiver = hid.device()
    try:
        receiver.open_path(receivers[0]["path"])
        deadline = monotonic() + args.timeout
        while monotonic() < deadline:
            remaining_ms = max(1, int((deadline - monotonic()) * 1000))
            report = receiver.read(3, min(remaining_ms, 250))
            sample = frame.consume(report, monotonic())
            if sample is not None:
                percent, charging = sample
                suffix = ", charging" if charging else ""
                print(f"NuPhy Halo96 V2 (2.4 GHz) {percent}%{suffix}")
                return
    except OSError as error:
        parser.exit(1, f"Cannot read the receiver: {error}\n")
    finally:
        receiver.close()
    parser.exit(1, "No complete battery frame received. Check the firmware and 2.4 GHz connection.\n")


if __name__ == "__main__":
    main()
