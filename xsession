#!/bin/sh

# Set touchpad, language, wallpaper, tranparecy
xinput set-prop "ELAN0504:00 04F3:3091 Touchpad" "libinput Tapping Enabled" 1
setxkbmap latam &
feh --bg-fill /home/jisas/.config/qtile/wallpapers/wallpaper.jpg &
picom -f &
