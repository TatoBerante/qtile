#!/bin/sh
setxkbmap latam &
nitrogen --restore &
picom -b --backend glx &
xdg-screensaver suspend 0x52b &
