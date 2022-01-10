#!/bin/bash
mkdir ~/Pictures/Screenshots/`date +%m-%Y` -p && 
scrot -s mode=edge --pointer -f ~/Pictures/Screenshots/try.png && 
xclip -selection clipboard -t image/png ~/Pictures/Screenshots/try.png && 
mv ~/Pictures/Screenshots/try.png ~/Pictures/Screenshots/`date +%m-%Y`/Screenshot_`date +%H:%M:%S_%d-%m-%Y`.png