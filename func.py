from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


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
