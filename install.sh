#!/bin/bash

# yay
sudo pacman -S git base-devel 

git clone http://aur.archlinux.org/yay-git.git && 
    cd yay git &&
    mkaepkg -si

# update
echo "want to update?"
echo "(y/n):" 
read update

if [[ $update == 'y' || $update == 'Y' ]]
then 
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
echo "Installing base install (imp)"
echo "======================================================================================"
sleep 1
yay -S xf86-video-ati lib32-mesa mandb xorg xorg-init picom-tryone-git kitty polkit acpi --needed

echo "======================================================================================"
echo "Installing fonts and emoji"
echo "======================================================================================"
sleep 1
yay -S ttf-nerd-fonts-symbols ttf-nerd-fonts-icons ttf-twemoji ttf-hack noto-font-emoji --needed

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
echo "Cleaning all cache and unused packages (won't cause much issue)"
echo "======================================================================================"
sleep 1
yay -Sc && yay -c

