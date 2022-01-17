#!/bin/fish

# compositor
picom --config ~/.config/picom/picom.conf -b --experimental-backends

# reload background
feh --bg-scale ~/.config/wallpapers/ring_dark.png

imwheel -b 45

# natural scroll
xinput set-button-map 8 1 2 3 5 4 6 7 8 9 10
