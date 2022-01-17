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
elif [[ $update != 'y' ]]
then
    echo "Not updating."
fi

# base install
yay -S xf86-video-ati lib32-mesa mandb xorg xorg-init picom-tryone-git kitty xorg-xinit polkit acpi alsamixer.app

# fonts
yay -S ttf-nerd-fonts-symbols ttf-nerd-fonts-icons ttf-twemoji ttf-hack noto-font-emoji

# terminal
yay -S fish bashtop neofetch lsd tmatrix rxfetch rofi neovim feh winetricks xdman man
# imp
yay -S qpdfview bleachbit vscodium-bin qtile qalculate-gtk xdman octave onlyoffice-desktopeditors scrot

# tp
yay -S smplayer spotify telegram qbittorrent smtube

# ungoogled chromium
curl -s 'https://download.opensuse.org/repositories/home:/ungoogled_chromium/Arch/x86_64/home_ungoogled_chromium_Arch.key' | sudo pacman-key -a -
echo '
[ungoogled_chromium_Arch]
SigLevel = Required TrustAll
Server = https://download.opensuse.org/repositories/home:/ungoogled_chromium/Arch/$arch' | sudo tee --append /etc/pacman.conf
sudo pacman -Sy

# skip startx
echo -n  "[[ $(fgconsole 2>/dev/null) == 1 ]] && exec startx --vt1" >> ~/.bash_profile

# clean
yay -Sc && yay -c

