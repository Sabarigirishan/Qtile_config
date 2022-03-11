#!/bin/bash
# numlockx

#   yay -S xf86-video-fbdev xorg xorg-xinit feh picom neovim kitty librewolf
#   yay -s openbox 
#   cp /etc/X11/xinitrc /home/sam/.xinitrc
#   remove these stuff from twm
#   feb --bg-scale wallpaper
#   picom &

echo "This script is currently for arch-linux, yay is necessary."
sleep 2

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
echo "xf86-video-ati, lib32-mesa, mandb, xorg, xorg-init, picom-tryone-git, kitty, nmtui, polkit, acpi, qt5ct, bluedevil, xorg-server, xterm, xautolock iputil xclip"
echo "======================================================================================"
sleep 1
yay -S xf86-video-ati lib32-mesa mandb lxappearance blueman-git qt5ct xorg-init picom-tryone-git kitty nmtui polkit acpi qt5ct ly xorg-server xterm xorg xautolock iputil xclip --needed

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
echo "zsh, bashtop, neofetch, lsd, tmatrix-git, rofi, neovim, feh, fzf, colorpicker, espeak, figlet, man, bat, cpufetch, curl, p7zip, cowsay, greed, colorpicker"
echo "======================================================================================"
sleep 1
yay -S zsh bashtop fish wallset ncdu neofetch lsd tmatrix-git rofi neovim feh fzf colorpicker figlet espeak man bat cpufetch curl p7zip cowsay greed colorpicker --needed

echo "======================================================================================"
echo "Installing tools for daily work:"
echo "qpdfview, bleachbit, vscodium-bin, qalculate-gtk, xdman, librewolf-bin, libreoffice-fresh, scrot, leafpad, i3lock-color-git, imagemagick, thunar"
echo "======================================================================================"
sleep 1
yay -S qpdfview bleachbit guvcview vscodium-bin qalculate-gtk xdman librewolf-bin libreoffice-fresh scrot leafpad i3lock-color-git imagemagick thunar --needed

echo "======================================================================================"
echo "Installing packages for entertainment purposes:"
echo "spotify,lltag, mpv, spicetify-cli, mpd, ncmpcpp, ytfzf, corny-jokes-git myman youplay 2048"
echo "======================================================================================"
sleep 1
yay -S spotify lltag spicetify-cli mpv mpd ncmpcpp ytfzf corny-jokes-git myman youplay 2048 --needed

echo "======================================================================================"
echo "Installing packages for entertainment purposes:"
echo "spotify, mpv, mpd, ncmpcpp, ytfzf, corny-jokes-git myman"
echo "======================================================================================"
sleep 1
yay -S rofi-calc rofi-bluetooth-git rofi-greenclip rofi-emoji rofi-calc --needed

echo "======================================================================================"
echo "Adding ungoogled-chromium-bin repo and Installing it:"
echo "Ungoogled-chromium"
echo "======================================================================================"
sleep 1
curl -s 'https://download.opensuse.org/repositories/home:/ungoogled_chromium/Arch/x86_64/home_ungoogled_chromium_Arch.key' | sudo pacman-key -a -
echo '
[Ungoogled-Chromium]
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

echo ">Android device mounting"
read optional
if [[ $optional == 'y' || $optional == 'Y' ]]
then
    yay -S mtpfs gvs-gphoto2 gvs-mpt --needed
fi

echo ">OCR support (python is also needed)"
read optional
if [[ $optional == 'y' || $optional == 'Y' ]]
then
    yay -S python-pip ocrmypdf --needed && pip install pdfplumber
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

# echo ">Select WM:"
# echo "1. Gnome"
# echo "2. Plasma"
# echo "3. Deepin"
# echo "4. Mate"
# echo "5. Skip"
# read DE
# case "$DE" in
#     "1") yay -S gnome --needed
#     ;;
#     "2") yay -S plasma-desktop sddm --needed
#     ;;
#     "3") yay -S deepin --needed
#     ;;
#     "4") yay -S mate --needed
#     ;;
#     "5") echo "Skipping."
# esac

echo "======================================================================================"
echo "Cleaning all cache and unused packages (won't cause much issue)"
echo "======================================================================================"
sleep 1
yay -Yc && yay -c && yay -Sc && sudo pacman -Rs $ (pacman -Qtdq)

echo "Want to config system on the go?"
echo "(y/n)"
read conf
if [[ $conf == 'y' || $conf == 'Y' ]]
then
    echo "======================================================================================"
    echo "Making few edits to config"
    echo "======================================================================================"
    sleep 1
    systemctl enable ly service
    sudo echo "ILoveCandy" > /etc/pacman.conf

fi
