#!/bin/bash
# numlockx

#   yay -S xf86-video-fbdev xorg xorg-xinit feh picom neovim kitty librewolf
#   install yay
#   base-devel
#   yay -s openbox 
#   cp /etc/X11/xinitrc /home/sam/.xinitrc
#   remove these stuff from twm
#   feb --bg-scale wallpaper
#   picom &
#   exec awesome
#
#	
#
#   
#   
#   
#   
#   

echo "This script is currently for arch-linux, yay is necessary. Try to remove packages wich are not needed"
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
    git clone http://aur.archlinux.org/yay-git.git 
        cd yay git
        mkaepkg -si
fi

echo "======================================================================================"
echo "Installing base install (imp):"
echo "xf86-video-ati, lib32-mesa, mandb, xorg, xorg-init, picom-tryone-git, kitty, polkit, acpi, qt5ct, bluedevil, lightdm, xorg-server, xterm "
echo "======================================================================================"
sleep 1
yay -S xf86-video-ati lib32-mesa mandb xorg xorg-init picom-tryone-git kitty polkit acpi qt5ct ly xorg-server xterm --needed

echo "======================================================================================"
echo "Installing packages related audio:"
echo "pulseaudio, pulsemixer, moc"
echo "======================================================================================"
sleep 1
yay -S pulseaudio pulsemixer moc --needed


echo "======================================================================================"
echo "Installing packages related to fonts and emoji:"
echo "ttf-nerd-fonts-symbols, ttf-nerd-fonts-icons, ttf-twemoji, ttf-hack, noto-font-emoji, x11-emoji-picker-git"
echo "======================================================================================"
sleep 1
yay -S ttf-nerd-fonts-symbols ttf-nerd-fonts-icons ttf-twemoji ttf-hack noto-font-emoji x11-emoji-picker-git --needed

echo "======================================================================================"
echo "Installing terminal based packages:"
echo "fish, bashtop, neofetch, lsd, tmatrix, rofi, neovim, feh, man, bat, curl, p7zip, cowsay, greed"
echo "======================================================================================"
sleep 1
yay -S fish bashtop neofetch lsd tmatrix rofi neovim feh xdman man bat curl p7zip cowsay greed --needed

echo "======================================================================================"
echo "Installing tools for daily work:"
echo "qpdfview, bleachbit, vscodium-bin, qalculate-gtk, xdman, onlyoffice-desktopeditors, scrot, thunar"
echo "======================================================================================"
sleep 1
yay -S qpdfview bleachbit vscodium-bin qalculate-gtk xdman onlyoffice-desktopeditors scrot thunar --needed

echo "======================================================================================"
echo "Installing packages for entertainment purposes:"
echo "smplayer, spotify, smtube"
echo "======================================================================================"
sleep 1
yay -S smplayer spotify smtube --needed

echo "======================================================================================"
echo "Adding and Installing ungoogled-chromium-bin:"
echo "Ungoogled-chromium"
echo "======================================================================================"
sleep 1
curl -s 'https://download.opensuse.org/repositories/home:/ungoogled_chromium/Arch/x86_64/home_ungoogled_chromium_Arch.key' | sudo pacman-key -a -
echo '
[home_ungoogled_chromium_Arch]
SigLevel = Required TrustAll
Server = https://download.opensuse.org/repositories/home:/ungoogled_chromium/Arch/$arch' | sudo tee --append /etc/pacman.conf
sudo pacman -Sy

echo "======================================================================================"
echo "Installing optional packages(These are really optional types)"
echo "======================================================================================"
sleep 1

echo "Want to install following packages (y/n):"
echo ">ttf-ms-fonts:"
read optional
if [[ $optional == 'y' || $optional == 'Y' ]]
then
    yay -S ttf-ms-fonts --needed
fi

echo ">rxfetch (fetch script)"
read optional
if [[ $optional == 'y' || $optional == 'Y' ]]
then
    yay -S rxfetch --needed
fi

echo ">GNU Octave"
read optional
if [[ $optional == 'y' || $optional == 'Y' ]]
then
    yay -S octave --needed
fi

echo ">Winetricks (it will install wine too)"
read optional
if [[ $optional == 'y' || $optional == 'Y' ]]
then
    yay -S winetricks --needed
fi

echo ">Font-manager-git"
read optional
if [[ $optional == 'y' || $optional == 'Y' ]]
then
    yay -S font-manager-git --needed
fi

echo ">tuir (Terminal reddit client)"
read optional
if [[ $optional == 'y' || $optional == 'Y' ]]
then
    yay -S tuir --needed
fi

echo ">ranger (Terminal file-manager)"
read optional
if [[ $optional == 'y' || $optional == 'Y' ]]
then
    yay -S ranger --needed
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
yay -Yc && yay -c && yay -Sc

