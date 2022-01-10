from typing import List  # noqa: F401
from libqtile.config import Key
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


# Autostart
import os
import subprocess
from libqtile import hook, qtile

# default apps
terminal = "kitty"
browser = "librewolf"
file_manager = "dolphin"
music = "spotify"
mod = "mod4"
home = os.path.expanduser("~")


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, "control"],
        "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    Key(
        [mod, "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle betq"een different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # app_launcher
    Key(
        ["mod1"],
        "space",
        lazy.spawn(
            "rofi -combi-modi drun -font 'Fira Code Nerd Font 12' -show drun -icon-theme 'Papirus' -show-icons -width 32"
        ),
    ),
    # Send window "go long"
    Key(
        [mod],
        "m",
        lazy.window.togroup("9", switch_group=True),
        desc="Switch to & move focused window to group {}".format("9"),
    ),
    #
    # To find what is the key name use xev
    # Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 5%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 5%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse sset Master toggle")),
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 5%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
    # xkill
    Key([mod], "x", lazy.spawn("xkill")),
    # rofi-power-menu
    Key(
        ["mod1", "control"],
        "Delete",
        lazy.spawn("rofi -show powermenu -modi powermenu:~/./rofi-power-menu"),
    ),
    # rofi-clipboard
    Key([mod], "v", lazy.spawn("rofi -show clipboard")),
    # rofi-calc
    Key([mod], "c", lazy.spawn("rofi -show calc")),
    # rofi-network-menu
    Key([mod], "W", lazy.spawn("./.config/qtile/rofi-wifi-menu")),
    # Key([mod, "control"], "Right", lazy.spawn(window_to_prev_group)),
    Key([mod], "b", lazy.spawn("librewolf --private-window")),
    # For file manager
    Key([mod], "e", lazy.spawn("dolphin")),
    # Screenshot-area
    Key(
        ["control"],
        "Print",
        lazy.spawn([home + "/.config/qtile/screenshot_a.sh"]),
    ),
    # Screenshot-window
    Key([], "Print", lazy.spawn([home + "/.config/qtile/screenshot_w.sh"])),
    # Screenshot-window
    Key([mod], "Print", lazy.spawn([home + "/.config/qtile/screenshot_d.sh"])),
]
