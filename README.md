# mister-boot-roms
Custom boot roms for the MiSTer FPGA project.
The MiSTer fpga project has cores that offer an interesting feature where you can boot into a rom upon starting it.
This project offers custimized roms to make some of the cores more interesting and fun.
Note: These are not bios replacement but only roms that are launched when booting a core.

Once I have tackled all the cores that can auto boot roms, I will release the source code and build instructions for people that want to do remixes.

If you want to contribute now, feel free to contact me on twitter. twitter.com/uberyoji

For more information about MiSTer please refer to the official wiki page: https://github.com/MiSTer-devel/Main_MiSTer/wiki

## How to install the boot roms
- Using the green 'Code' button from the main repo page, select 'Download ZIP'
- Extract the 'Games' folder in /media/fat on your mister sd card.

#### So far only the following core roms are available:
- NES (boot1.rom)  
![NES](Images/NES.gif)
- Nintendo Gameboy (boot2.rom)  
![Gameboy](Images/gameboy.gif)
- NEC PC Engine (boot.rom)
![PCE](Images/pce.gif)
- Sega Master System (boot.rom) WIP (Issue with bios. Disable in menu to have it launch properly on core boot.)
![SMS](Images/sms.gif)
- Sega Genesis (boot.rom) WIP

#### Planned core roms:
- SNES (boot.rom)
- GBA (boot.rom) WIP. Unreleased since the boot support in MiSTer is not working :-/ See this: https://github.com/MiSTer-devel/GBA_MiSTer/issues/87


#### General TODO:
- Clean and upload source code.
- Add build steps for each roms.
- Brainstorm some ideas
- Add more variations, fx, interactivity

#### TODO: NES
- Add more scenes
- Add sram support to save scene config

#### TODO: Gameboy
- Add more scenes
- Add sram support to save scene config
 
#### TODO: PC Engine
- Add more scenes
- Add sram support to save scene config

#### TODO: SMS
- Add more scenes
- Add sram support to save scene config
- Fix issue with bios turned on
 

Feel free to contact me via the issues if you have comments, suggestions, feedback.
