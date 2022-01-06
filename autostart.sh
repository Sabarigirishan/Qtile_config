#!/bin/fish

# compositor
picom --config ~/.config/picom/picom.conf

# reload background
feh --bg-scale 'Downloads/Compressed/wallpaper-master/manjaro.png'

imwheel -b 45

# natural scroll
xinput set-button-map 8 1 2 3 5 4 6 7 8 9 10
