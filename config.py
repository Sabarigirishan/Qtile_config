from key import *
from layout import *
from libqtile.log_utils import logger
from libqtile.dgroups import simple_key_binder

import os
import subprocess


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


mod = "mod4"


widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

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

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = "LG3D"


groups = [
    Group("🥳", layout="columns", matches=[Match(wm_class=["Spotify"])]),
    Group(
        "🙇🏻‍♂️",
        layout="columns",
        matches=[
            Match(wm_class=["Microsoft Teams - Preview"]),
        ],
    ),
    Group("🥱", layout="columns"),
    Group("🗑", layout="columns"),
    Group("5", layout="columns"),
    Group("6", layout="columns"),
    Group("7", layout="columns"),
    Group("8", layout="columns"),
    Group("9", layout="columns"),
]

dgroups_key_binder = simple_key_binder(mod)
