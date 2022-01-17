#!/bin/bash

echo "This script is currently for arch-linux, yay is necessary."
sleep 2

echo "want to update?"
echo "(y/n):" 
read update

if [[ $update == 'y' || $update == 'Y' ]]
then 
    echo "======================================================================================"
    echo "Installing updating"
    echo "======================================================================================"
    sleep 1

    yay -Syu
    echo "Want to reboot?"
    echo "(y/n):"
    read reb
    if [[ $reb == 'y' || $reb == 'Y' ]]
    then 
        sudo reboot
    fi
elif [[ $update != 'y' ]]
then
    echo "Not updating."
fi

echo "======================================================================================"
echo "Installing base-devel(imp)"
echo "======================================================================================"
sleep 1
sudo pacman -S git base-devel --needed

echo "Want to install yay?"
echo "(y/n):" 
read y_install

if [[ $y_install == 'y' || $y_install == 'Y' ]]
then 
    echo "======================================================================================"
    echo "Installing yay (imp)"
    echo "======================================================================================"
    sleep 1
    git clone http://aur.archlinux.org/yay-git.git && 
        cd yay git &&
        mkaepkg -si
fi

echo "======================================================================================"
echo "Installing base install (imp)"
echo "======================================================================================"
sleep 1
yay -S xf86-video-ati lib32-mesa mandb xorg xorg-init picom-tryone-git kitty polkit acpi --needed

echo "======================================================================================"
echo "Installing packages related to fonts and emoji"
echo "======================================================================================"
sleep 1
yay -S ttf-nerd-fonts-symbols ttf-nerd-fonts-icons ttf-twemoji ttf-hack noto-font-emoji x11-emoji-picker-git --needed

echo "======================================================================================"
echo "Installing terminal based packages"
echo "======================================================================================"
sleep 1
yay -S fish bashtop neofetch lsd tmatrix rxfetch rofi neovim feh winetricks xdman man --needed

echo "======================================================================================"
echo "Installing tools for daily work"
echo "======================================================================================"
sleep 1
yay -S qpdfview bleachbit vscodium-bin qtile qalculate-gtk xdman octave onlyoffice-desktopeditors scrot --needed

echo "======================================================================================"
echo "Installing packages for entertainment purposes"
echo "======================================================================================"
sleep 1
yay -S smplayer spotify telegram qbittorrent smtube --needed

echo "======================================================================================"
echo "Installing optional packages(These are really optional types)"
echo "======================================================================================"
sleep 1

echo "Want to install following packages (y/n):"
echo ">ttf-ms-fonts:"
read optional_1
if [[ $optional_1 == 'y' || $optional_1 == 'Y' ]]
then
    yay -S ttf-ms-fonts --needed
fi

echo "======================================================================================"
echo "Installing WM"
echo "======================================================================================"
sleep 1

echo ">Select WM:"
echo "1. Awesome"
echo "2. Qtile"
echo "3. I3"
echo "4. dwm"
echo "5. Skip"
read WM
case "$WM" in
    "1") yay -S awesome --needed
    ;;
    "2") yay -S qtile --needed
    ;;
    "3") yay -S i3 --needed
    ;;
    "4") yay -S dwm --needed
    ;;
    "5") echo "Skipping."
esac

echo "======================================================================================"
echo "Installing DE"
echo "======================================================================================"
sleep 1

echo ">Select WM:"
echo "1. Gnome"
echo "2. Plasma"
echo "3. Deepin"
echo "4. Mate"
echo "5. Skip"
read DE
case "$DE" in
    "1") yay -S gnome --needed
    ;;
    "2") yay -S plasma-desktop sddm --needed
    ;;
    "3") yay -S deepin --needed
    ;;
    "4") yay -S mate --needed
    ;;
    "5") echo "Skipping."
esac



echo "======================================================================================"
echo "Cleaning all cache and unused packages (won't cause much issue)"
echo "======================================================================================"
sleep 1
yay -Sc && yay -c

