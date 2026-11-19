# Halo96 V2 battery telemetry over 2.4 GHz

The goal is to report a live battery percentage to Windows while the keyboard stays connected to its 2.4 GHz receiver. The first target is the QMK/VIA Halo96 V2 ANSI (`nuphy/halo96_v2/ansi`, keymap `via`). The checkout starts from [NuPhy's published QMK source at f185691](https://github.com/nuphy-src/qmk_firmware/tree/f1856912d603800eaca227ae2e1c5c8548fdf261). Its equivalence to the factory QMK binary has not been verified.

## Hardware and firmware observations

- The connected receiver is `19F5:3247`, USB revision `0209`. Its vendor HID collection is `FF31:0074` on interface 2. Windows reports 65-byte input and output reports, including the report ID, and zero feature reports. None of the six HID collections declares a standard battery value.
- The stock keyboard reported 66% to the Windows battery monitor over Bluetooth. With the keyboard in 2.4 GHz mode, the same monitor returned no reading.
- The dongle image contained in [NuPhy's Windows v2.1.5 updater](https://pay.nuphy.com/pages/qmk-firmwares) matches those USB identifiers and descriptors. Static inspection found a path that relays some radio replies to the vendor USB input endpoint. No battery command or matching reply has been verified.
- The keyboard receives the percentage and charge flags from the onboard radio module. It initializes the display value to 100% at startup and can substitute 100% based on a charge flag. Host telemetry needs a fresh, validated status sample so the app can distinguish a genuine 100% reading from a default or stale value. [Startup state](../keyboards/nuphy/halo96_v2/ansi/ansi.c#L24) · [Wireless status handler](../keyboards/nuphy/halo96_v2/ansi/rf.c#L250)

## Experimental implementation

Static inspection of the v2.1.5 radio and dongle images found that the keyboard radio forwards the two-byte Consumer Control value from QMK over 2.4 GHz and the receiver sends it on USB report ID `03`. This build reuses that path with reserved Consumer Control usages. The build samples the raw radio-reported percentage and transmits about once every 15 seconds while connected and awake in 2.4 GHz mode. Physical media keys take priority and cancel a frame in progress. [USB HID Usage Tables, Consumer page](https://usb.org/sites/default/files/hut1_5.pdf)

The four usage values in a frame are `07`, `08 + (percent >> 4)`, `10 + (percent & 0F)`, and the normal zero release, shown in hexadecimal. Each value is carried in a separate input report, with a minimum 50 ms between reports. The reader accepts complete frames within 500 ms and checks the 0–100 range. Windows shares access to the Consumer Control collection with applications. [Windows HID collection access](https://learn.microsoft.com/en-us/windows-hardware/drivers/hid/top-level-collections-opened-by-windows-for-system-use)

The charging build adds an optional `0F` usage immediately before `07` when the radio status is `03`, the same active-charging flag the keyboard uses for its indicator. Earlier readers still receive the four percentage usages. [Stock indicator logic](../keyboards/nuphy/halo96_v2/ansi/side.c#L1024)

## Build and test

Build from a configured QMK environment with the pinned dependencies and telemetry enabled.

```sh
git submodule update --init -- lib/chibios lib/chibios-contrib lib/lufa lib/printf
make SKIP_GIT=yes nuphy/halo96_v2/ansi:via TARGET=nuphy_halo96_v2_ansi_battery_debounce NUPHY_BATTERY_TELEMETRY=yes
```

Flash `nuphy_halo96_v2_ansi_battery_debounce.bin` to the **Halo96 V2 QMK/VIA ANSI** keyboard using QMK Toolbox over USB. Leave the onboard radio and dongle on their factory firmware. NuPhy provides the stock ANSI v2.1.5 keyboard binary for rollback through the same flash procedure. [NuPhy flashing guide](https://nuphy.com/pages/update-instructions) · [Stock keyboard firmware](https://cdn.shopify.com/s/files/1/0268/7297/1373/files/QMK_firmware_nuphy_halo96_v2_ansi_v2.1.5.bin?v=1741067981)

Switch the keyboard to wireless, tap **Fn + 4**, and run the read-only test from the repository in PowerShell.

```powershell
uv run --script .\util\read_halo96_battery.py
```

The reader prints the first battery percentage or times out after 25 seconds. To check charging, plug in the USB cable while the keyboard stays in wireless mode on the 2.4 GHz channel. The reading should show `charging` while a partially depleted battery is charging. Run the reader again after unplugging to verify that the label clears.

The charging release reported `78%, charging` on a Halo96 V2 QMK/VIA ANSI through its original receiver.
