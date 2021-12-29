from libqtile import hook
from libqtile.lazy import lazy
from libqtile import qtile
from libqtile.lazy import lazy

wifi_menu = "~/.local/bin/rofi-wifi-menu /usr/share/rofi/themes/dracula.rasi"


def rofi_power_menu():
    qtile.cmd_spawn("rofi -show power-menu")


def play_pause(qtile):
    qtile.cmd_spawn("playerctl -p spotify play-pause")
    qtile.cmd_spawn("playerctl -p ncspot play-pause")
    qtile.cmd_spawn("playerctl -p vlc play-pause")


def nexts(qtile):
    qtile.cmd_spawn("playerctl -p spotify next")
    qtile.cmd_spawn("playerctl -p ncspot next")
    qtile.cmd_spawn("playerctl -p vlc next")


def prev(qtile):
    qtile.cmd_spawn("playerctl -p spotify previous")
    qtile.cmd_spawn("playerctl -p ncspot previous")
    qtile.cmd_spawn("playerctl -p vlc previous")


def stop(qtile):
    qtile.cmd_spawn("playerctl -p spotify stop")
    qtile.cmd_spawn("playerctl -p ncspot stop")
    qtile.cmd_spawn("playerctl -p vlc stop")


@hook.subscribe.startup_once
def start_once():
    subprocess.call("~/.config.qtile/autostart,sh")


def rofi_network_menu():
    qtile.cmd_spawn("./.config/qtile/rofi-wifi-menu")
