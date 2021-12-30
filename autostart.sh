#!/bin/fish

# compositor
picom --experimental-backend &

# reload background
nitrogen --restore &

imwheel -b 45

# natural scroll
xinput set-button-map 8 1 2 3 5 4 6 7 8 9 10

# pending
# screenshot tool spectacle from kde here -l is to just launch and -b is for to launch in background
# spectacle -l -b 

# for emoji suggestion
emote