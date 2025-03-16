# Custom Split Keyboard using Raspberry Pi Pico and KMK firmware

<br/><br/>

> [!WARNING]
>
> This is a work in progress, as I'm waiting for the part to arrive.
>
> **Coming soon**&trade;&copy;

<br/><br/>

<div align='center'>

[![GitHub License](https://img.shields.io/github/license/revalew/Split-Keeb?style=social)](https://github.com/revalew/Split-Keeb/blob/master/LICENSE)

[![GitHub](https://img.shields.io/github/commit-activity/t/revalew/Split-Keeb?style=social)](https://github.com/revalew/Split-Keeb)
[![GitHub](https://img.shields.io/github/last-commit/revalew/Split-Keeb?style=social)](https://github.com/revalew/Split-Keeb)

[![GitHub](https://img.shields.io/github/repo-size/revalew/Split-Keeb?style=social)](https://github.com/revalew/Split-Keeb) [![GitHub](https://img.shields.io/github/languages/top/revalew/Split-Keeb?style=social)](https://github.com/revalew/Split-Keeb)

</div>

<br/><br/>

# Table of Contents

<br/>

1. [`Overview`](#overview)


2. [`Required / used components`](#required--used-components)


3. [`Project structure and important locations`](#project-structure-and-important-locations)

<br/><br/>

# Overview

<br/>

The aim of this project is to create a custom split keyboard using [`KMK firmware`](https://github.com/KMKfw/kmk_firmware/) and a [`Raspberry Pi Pico 2`](https://www.waveshare.com/product/rp2350-plus.htm).
This is my first attempt at creating a custom keyboard, and I'm excited to see how it turns out.

<br/><br/>

## Required / used components

<br/>

> [!CAUTION]
>
> NOT FULLY READY YET - EMPTY LINKS!
> 
> **Coming soon**&trade;&copy;

<!-- https://scottokeebs.com/blogs/keyboards/scotto44-handwired-keyboard -->

<br/>

- [`2x Raspberry Pi Pico 2`](https://www.waveshare.com/product/rp2350-plus.htm)

<br/>

- [`2x USB-C breakout board for UART communication between split modules`](#)

<br/>

- [`Xx switches`](#)

<br/>

- [`Xx keycaps (1 for each switch)`](#)

<br/>

- [`Xx diodes (1N4148, 1 for each switch)`](https://www.digikey.pl/pl/products/detail/onsemi/1N4148/458603)

<br/>

- `1x USB-C to USB-C cable` (connect both modules) and `1x USB-C to USB-A cable` (connect the keyboard to the computer from either side, can be swapped out for a USB-C to USB-C cable)

<br/>

- `soldering iron and solder`

<br/>

- `wires`

<br/>

- `heat shrink tubes`

<br/>

- [`3D printed enclosure for the device to protect the circuit`](#)

<br/><br/>

## Project structure and important locations

<br/>

- [`~/.ALL`](./.ALL/) - Directory containing the docs, examples and KMK repository (read the [README](./.ALL/README.md) there),

<br/>

- [`~/libs_to_compile/`](./libs_to_compile/) - Directory containing all the libraries (before compilation) and instructions on how to compile them along with the scripts to do it. In my project, I provide the KMK library as a symlink, but the scripts also work with the symlinked library (read the [README](./libs_to_compile/README.md) there),

  - [`~/libs_to_compile/lib/`](./libs_to_compile/lib/) - Directory containing the libraries and custom classes (before compilation),

  - [`~/libs_to_compile/lib/classes/`](./libs_to_compile/lib/classes/) - Directory (module) containing all necessary custom-written classes for easy development.

<br/>

- [`~/src/`](./src/) - Directory containing the compiled libraries and the code of the project (directory to sync to the Pico - `"micropico.syncFolder": "src",`),

  - [`lib/`](./src/lib/) - Directory containing all the libraries after compilation.

  - [**`boot.py`**](./src/boot.py) - The file that runs before the main program, used to configure the keyboard,

  - [**`main.py`**](./src/main.py) - The main file of the project and the program to be executed on startup,

<br/>

- [`~/Makefile`](./Makefile) - The file for automating the `git` workflow (committing, pushing, adding new tags, etc.),

<br/><br/>

### ...

<br/><br/>
