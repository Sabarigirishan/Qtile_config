# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401
from key import *

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"

layout_theme = {
    "border_width": 4,
    "margin": 8,
    "border_focus": "cyan",
}
# border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4
layouts = [
    layout.Columns(**layout_theme),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=1, **layout_theme),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.WindowName(
                    font="SF Pro Display",
                    fontsize=10,
                    format="{name}",
                    max_chars=25,
                ),
                widget.Systray(icon_size=18),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=20,
                ),
                widget.Image(
                    filename="~/Downloads/logo.png",
                    # mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("/home/sam/.config/rofi/powermenu/powermenu.sh")},
                    margin=3,
                ),
            ],
            24,
        ),
        bottom=bar.Bar(
            [
                widget.GroupBox(),
                widget.Sep(linewidth=0, padding=8),
                widget.CurrentLayoutIcon(scale=0.80),
                widget.Prompt(),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=20,
                ),
                widget.TextBox(
                    text="",
                    font="FontAwesome 5 Free",
                    fontsize=18,
                ),
                widget.PulseVolume(
                    font="FiraCode Nerd Font",
                ),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=20,
                ),
                widget.TextBox(
                    font="FiraCode Nerd Font",
                    fontsize=18,
                    text="",
                ),
                widget.Clock(
                    font="FiraCode Nerd Font",
                    fontsize=12,
                    format="%d-%m-%y",
                ),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=20,
                ),
                widget.TextBox(
                    font="FiraCode Nerd Font",
                    fontsize=18,
                    text="",
                ),
                widget.Clock(
                    format="%a %I:%M %p",
                ),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=20,
                ),
                # widget.QuickExit(),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# here all auto start part is
# lazy.to_screen(n) here n is desktop number i think
# lazy.spawn("name") here name is command name
def autostart():
    lazy.to_screen(0)
    lazy.spawn("picom")


widget_defaults = dict(
    font="Fira Code Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
