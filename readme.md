# NuPhy Halo96 V2 battery telemetry

Custom QMK firmware for the **NuPhy Halo96 V2 QMK/VIA ANSI**. It sends the keyboard's battery percentage and active charging state over the original 2.4 GHz USB receiver (`19F5:3247`).

## Install

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
- [v0.1.1 release notes](docs/releases/v0.1.1.md)
- [v0.1.0 release notes](docs/releases/v0.1.0.md)

This project is based on [NuPhy's published QMK source](https://github.com/nuphy-src/qmk_firmware/tree/f1856912d603800eaca227ae2e1c5c8548fdf261). The [GPLv2 license](LICENSE) and upstream notices are retained.

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
