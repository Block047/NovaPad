# NovaPad

NovaPad is a fully customizable and open sourced macropad that I had designed for fun in my spare time.

NovaPad was designed as a multi-purpose tool, allowing for it to aid in any task at hand.

## Features
Fully customizable:
 - EC11 Rotary Encoder Switch
 - 6 Keys
 - WS2812B RGB LED's for each key
 - 128x32 OLED screens 

## Housing
The housing is split into two parts, the top lid of the case, and the lower case itself.
The PCB is secured to the case using two M3 heated inserts vertically, and the lid is secured to the case using three horizontal self-tapping screws.

<img src=assets/case.png alt ="Case" width="500"/>

Made in OnShape

## PCB
<img src=assets/pcb-design.png alt="Design" width="500"/>
<img src=assets/pcb.png alt="PCB" width="500"/>

The PCB intergrates the various components included in the project, allowing them to communicate with one another, giving the keyboard its functionality.
Designing the PCB consisted of organizing the components in the positions that I wanted them in, and then drawing the trace lines, which took hours of work left untracked in hacktime (I was trying to use wakatime to track it, which ended up not working.)

## Schematic
<img src=assets/schematic.png alt="Schematic" width="500"/>

The schematic had been the easiest part of the project, only specifying what connected to what.
The only decently difficult part of designing the schematic was figuring out where and how to get the footprints for the various components that KiCad didn't have, and figuring out how to wire the keyboard matrix.

## Firmware
This project uses KMK python code, running on the XIAO microcontroller provided by stardance flashed with CircuitPython.
The firmware leaves much for customization, the default functions only being a simple number pad with a volume knob, the OLED displaying "NovaPad".
This configuration was designed to be customized, giving the user flexability and functionality when needed.
