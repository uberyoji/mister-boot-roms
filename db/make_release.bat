echo off
if exist release\ (
  rmdir /S /Q release 
)

echo Building file structure
mkdir release
mkdir release\games
mkdir "release\_Console (autoboot)"

copy *.mgl "release\_Console (autoboot)"

mkdir release\games\Gameboy
mkdir release\games\MegaDrive
mkdir release\games\SMS
mkdir release\games\NES
mkdir release\games\SNES
mkdir release\games\S32X
mkdir release\games\TGFX16

copy mister-boot.gb release\games\Gameboy
copy mister-boot.md release\games\MegaDrive
copy mister-boot.sms release\games\SMS
copy mister-boot.nes release\games\NES
copy mister-boot.sfc release\games\SNES
copy mister-boot.32x release\games\S32X
copy mister-boot.pce release\games\TGFX16

echo Building Archive
tar.exe -C release\ -a -cf mister-boot-roms-mgl.zip *

echo Cleaning Up
rmdir /S /Q release

echo Done