from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen

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
                widget.Clock(
                    format="%a %I:%M %p",
                ),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=20,
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
                widget.Spacer(),
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
                    format="%d-%b-%y",
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
                # widget.QuickExit(),
            ],
            24,
        ),
    ),
]
