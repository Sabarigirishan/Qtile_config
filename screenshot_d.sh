#!/bin/bash
mkdir ~/Pictures/Screenshots/`date +%m-%Y` -p && 
scrot --pointer ~/Pictures/Screenshots/try.png && 
xclip < ~/Pictures/Screenshots/try.png && 
mv ~/Pictures/Screenshots/try.png ~/Pictures/Screenshots/`date +%m-%Y`/Screenshot_`date +%H:%M:%S_%d-%m-%Y`.png
