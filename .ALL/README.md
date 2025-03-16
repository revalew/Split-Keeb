# Structure of `.ALL`

<br/><br/>

This directory contains all the documentation, KMK repo, and examples

<br/><br/>

## `.ALL/`

<br/>

- [`architecture_check.py`](./architecture_check.py) - Script to check the architecture of the Pico (`armv6m`, `armv7emsp`, etc. - required for the `.mpy` compilation),

<br/><br/>

## `docs/`

<br/>

- [`rename_pico/`](./docs/rename_pico/) - Renaming the Pico to a different name (required for the split keyboard to automatically detect the master device),

<br/>

- [`RP2350-Plus/`](./RP2350-Plus/) - Documentation, schematics, and `CircuitPython` firmware for the Waveshare RP2350-Plus,

<br/>

- [`boot.md`](./docs/boot.md) - Boot configuration for the KMK keyboard using the provided `bootcfg` function,

<br/>

- [`porting_to_kmk.md`](./docs/porting_to_kmk.md) - Porting your keyboard to KMK (**`coord_mapping`** example),

<br/>

- [`MARKDOWN_FORMATTING.png`](./docs/MARKDOWN_FORMATTING.png) - Markdown Alerts formatting,

<br/>

- [`pico_usb_c_mod.jpg`](./docs/pico_usb_c_mod.jpg) - Simple diagram of the Pico's test pins and USB-C connector (add USB-C connector to the Pico),

<br/>

- [`SYMLINKS.md`](./docs/SYMLINKS.md) - Symbolic links to the KMK repo and examples.

<br/><br/>

## `examples/`

<br/>

- [`Scotto_examples/`](./examples/Scotto_examples/) - KMK examples (and more) by `Joe Scotto`: [`GitHub`](https://github.com/joe-scotto/scottokeebs),

<br/>

- [`tinyboatproductions/`](./examples/tinyboatproductions/) - Custom Pico Numpad using KMK, example by `Tiny Boat Productions`: [`YouTube`](https://www.youtube.com/@tinyboatproductions), [`Instructables`](https://www.instructables.com/member/tinyboatproductions/instructables/),

<br/>

- [`Hand_Wiring_Guide_QMK_Firmware.pdf`](./examples/Hand_Wiring_Guide_QMK_Firmware.pdf) / [`Hand_Wiring_Guide_QMK_Firmware.png`](./examples/Hand_Wiring_Guide_QMK_Firmware.png) - Hand-wiring guide from `QMK` documentation: [`website`](https://docs.qmk.fm/hand_wire),

<br/>

- [`How_To_Split_Keyboard_with_RP2040_and_KMK.pdf`](./examples/How_To_Split_Keyboard_with_RP2040_and_KMK.pdf) / [`How_To_Split_Keyboard_with_RP2040_and_KMK.png`](./examples/How_To_Split_Keyboard_with_RP2040_and_KMK.png) - How to split a keyboard with the RP2040 and KMK firmware by `Sanderg.nl`: [`website`](https://sanderg.nl/en/posts/how-to-split-keyboard-with-rp2040-and-kmk/).

<br/><br/>

## `kmk_repo/`

<br/>

- [`README.md`](./kmk_repo/README.md) - instruction for configuring a submodule as a Separate Branch (`1:1` Copy),

<br/>

- [`Makefile`](./kmk_repo/Makefile) - Makefile fetching the updates from the KMK repository and copying them `1:1` to a separate branch in my repository,

<br/>

- [`kmk_firmware/`](./kmk_repo/kmk_firmware/) - KMK repository with required code, documentation, and tools,

  - [`/docs/en/`](./kmk_repo/kmk_firmware/docs/en/) - Full KMK documentation,

  - [`/kmk/`](./kmk_repo/kmk_firmware/kmk/) - KMK library.

<br/><br/>
