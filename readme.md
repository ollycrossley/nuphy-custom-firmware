# NuPhy Halo96 V2 battery telemetry

> **Unofficial firmware.** This is a community-developed firmware modification. It is not affiliated with, endorsed by, or supported by NuPhy.

Custom QMK firmware for the **NuPhy Halo96 V2 QMK/VIA ANSI**. It sends the keyboard's battery percentage and active charging state over the original 2.4 GHz USB receiver (`19F5:3247`).

## Install

> **Flashing warning.** Flash at your own risk. An incorrect firmware image or an interrupted update can leave the keyboard unusable. Confirm you have the QMK/VIA ANSI edition and keep the official keyboard firmware available for recovery.

1. Download `nuphy_halo96_v2_ansi_battery_debounce.bin` and `SHA256SUMS.txt`. Confirm your keyboard is the QMK/VIA ANSI edition with the single-row Enter key. [Latest firmware release](https://github.com/ollycrossley/nuphy-custom-firmware/releases/latest)
2. Flash the `.bin` to the **keyboard** over USB using QMK Toolbox. The build targets the factory v2.1.5 radio and receiver firmware. [NuPhy flashing guide](https://nuphy.com/pages/update-instructions)
3. Switch to **Wireless** and tap **Fn + 4**. Use a battery-monitor build that supports the custom Halo96 V2 reports. Displaying active charging requires charging support in the app as well.

Use this command in PowerShell to compare the downloaded firmware with `SHA256SUMS.txt`.

```powershell
Get-FileHash .\nuphy_halo96_v2_ansi_battery_debounce.bin -Algorithm SHA256
```

## Test and recover

Run the standalone Windows reader from the repository with [uv](https://docs.astral.sh/uv/).

```powershell
uv run --script .\util\read_halo96_battery.py
```

Keep the keyboard awake on 2.4 GHz and connect the charging cable. The reader waits up to 25 seconds for one sample. It has reported `78%, charging` on a Halo96 V2 using the stock receiver.

To restore factory behavior, flash the official ANSI keyboard firmware with the same QMK Toolbox procedure. [NuPhy firmware downloads](https://pay.nuphy.com/pages/qmk-firmwares)

## Source and releases

- [Protocol, build command, and test procedure](docs/halo96-v2-battery-telemetry.md)
- [v0.1.1 release notes](docs/releases/v0.1.1.md) · [Corresponding source](https://github.com/ollycrossley/nuphy-custom-firmware/tree/f88120dd07ceafc089bf591fe58c25dfcd12de32)
- [v0.1.0 release notes](docs/releases/v0.1.0.md) · [Corresponding source](https://github.com/ollycrossley/nuphy-custom-firmware/tree/1342d46b9b512bc2cb4ecf94a65080668716aa56)

NuPhy provided the Halo96 V2 board support in [its QMK firmware fork](https://github.com/nuphy-src/qmk_firmware). This project builds on [NuPhy's published source at f185691](https://github.com/nuphy-src/qmk_firmware/tree/f1856912d603800eaca227ae2e1c5c8548fdf261) and the work of the original [QMK Firmware project](https://github.com/qmk/qmk_firmware) and its contributors.

## Licence and warranty

The repository retains the upstream [GNU General Public License, version 2](LICENSE) text, copyright notices, and licence files. The Halo96 V2 source files with GPL version 2-or-later notices retain that option. Dependencies, including [ChibiOS](https://github.com/qmk/ChibiOS/tree/be44b3305f9a9fe5f2f49a4e7b978db322dc463e), carry their own licence terms and notices.

The firmware is provided as is, without warranty, including any implied warranty of merchantability or fitness for a particular purpose, to the extent permitted by applicable law.

## Upstream QMK

[![Current Version](https://img.shields.io/github/tag/qmk/qmk_firmware.svg)](https://github.com/qmk/qmk_firmware/tags)
[![Discord](https://img.shields.io/discord/440868230475677696.svg)](https://discord.gg/Uq7gcHh)
[![Docs Status](https://img.shields.io/badge/docs-ready-orange.svg)](https://docs.qmk.fm)
[![GitHub contributors](https://img.shields.io/github/contributors/qmk/qmk_firmware.svg)](https://github.com/qmk/qmk_firmware/pulse/monthly)
[![GitHub forks](https://img.shields.io/github/forks/qmk/qmk_firmware.svg?style=social&label=Fork)](https://github.com/qmk/qmk_firmware/)

This is a keyboard firmware based on the [tmk\_keyboard firmware](https://github.com/tmk/tmk_keyboard) with some useful features for Atmel AVR and ARM controllers, and more specifically, the [OLKB product line](https://olkb.com), the [ErgoDox EZ](https://ergodox-ez.com) keyboard, and the Clueboard product line.

## Documentation

* [See the official documentation on docs.qmk.fm](https://docs.qmk.fm)

The docs are powered by [Docsify](https://docsify.js.org/) and hosted on [GitHub](/docs/). They are also viewable offline; see [Previewing the Documentation](https://docs.qmk.fm/#/contributing?id=previewing-the-documentation) for more details.

## Supported Keyboards

* [Planck](/keyboards/planck/)
* [Preonic](/keyboards/preonic/)
* [ErgoDox EZ](/keyboards/ergodox_ez/)
* [Clueboard](/keyboards/clueboard/)
* [Cluepad](/keyboards/clueboard/17/)
* [Atreus](/keyboards/atreus/)

The project also includes community support for [lots of other keyboards](/keyboards/).

## Maintainers

QMK is developed and maintained by Jack Humbert of OLKB with contributions from the community, and of course, [Hasu](https://github.com/tmk). The OLKB product firmwares are maintained by [Jack Humbert](https://github.com/jackhumbert), the Ergodox EZ by [ZSA Technology Labs](https://github.com/zsa), the Clueboard by [Zach White](https://github.com/skullydazed), and the Atreus by [Phil Hagelberg](https://github.com/technomancy).

## Official Website

[qmk.fm](https://qmk.fm) is the official website of QMK, where you can find links to this page, the documentation, and the keyboards supported by QMK.
