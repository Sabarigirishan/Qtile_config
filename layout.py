from libqtile import bar, layout, widget

from libqtile.config import Match, Screen

from libqtile.widget import *


layout_theme = {
    "border_width": 3,
    "margin": 8,
    "border_focus": "e1acff",
    "border_normal": "1D2330",
}
# border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4
layouts = [
    layout.Stack(num_stacks=1, **layout_theme),
    layout.Columns(**layout_theme),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


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
        Match(wm_class="Qalculate-gtk"),
    ]
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=10,
                ),
                widget.WindowName(
                    font="FiraCode Nerd Font",
                    fontsize=12,
                    format="{name}",
                    max_chars=25,
                ),
                widget.Clock(
                    format="%a %I:%M %p",
                ),
                widget.Spacer(),
                widget.Systray(icon_size=18),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=20,
                ),
                widget.Image(
                    filename="~/Downloads/logo.png",
                    mouse_callbacks={
                        "Button1": "rofi -show powermenu -modi powermenr:~/./rofi-power-menu"
                    },
                    margin=3,
                ),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=10,
                ),
            ],
            24,
        ),
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    font="FiraCode Nerd Font",
                    fontsize=10,
                ),
                widget.Sep(linewidth=0, padding=8),
                widget.CurrentLayoutIcon(scale=0.80),
                widget.CurrentLayout(),
                widget.Prompt(),
                widget.Spacer(),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=20,
                ),
                widget.Net(
                    font="FiraCode Nerd Font",
                    fontsize=12,
                    format=" {down}⬇:⬆{up}",
                    prefix="b",
                    mouse_callbacks={"Button1": "./.config/qtile/rofi-wifi-menu"},
                ),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=20,
                ),
                widget.TextBox(
                    text="💡",
                ),
                widget.Backlight(
                    font="FiraCode Nerd Font",
                    brightness_file="/sys/class/backlight/amdgpu_bl0/brightness",
                    backlight_name="amdgpu_bl0",
                ),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=10,
                ),
                widget.TextBox(
                    text="📢",
                ),
                widget.PulseVolume(
                    font="FiraCode Nerd Font",
                ),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=10,
                ),
                widget.TextBox(
                    text="⚡",
                ),
                widget.Battery(
                    font="FiraCode Nerd Font",
                    fontsize=12,
                    update_interval=30,
                    show_short_text=False,
                    format="{percent:1.0%}",
                ),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=10,
                ),
                widget.TextBox(
                    text="📆",
                ),
                widget.Clock(
                    font="FiraCode Nerd Font",
                    fontsize=12,
                    format="%d-%b-%y",
                ),
                # widget.QuickExit(),
            ],
            24,
        ),
    ),
]
