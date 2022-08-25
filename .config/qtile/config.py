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

import os
import subprocess

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "alacritty"


# Colors as a dictionary:
colors = dict(
    transparent = "#00000000",
    black       = "#000000",
    dark_grey   = "#333333",
    white       = "#bfbfbf",
    true_white  = "#ffffff",
    red         = "#d54e53",
    orange      = "#fa7b05",
    yellow      = "#e7c547",
    green       = "#b9ca4a",
    aqua        = "#70c0b1",
    blue        = "#7aa6da",
    purple      = "#c397d8",
)


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    #Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
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
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    #Key([mod], "r", lazy.run_extension(extension.Dmenu(
    #    dmenu_prompt=">",
    #    dmenu_command='dmenu_run',
    #    dmenu_font='JetBrainsMonoMedium Nerd Font Mono-10',
    #))),
    Key([mod], "space", lazy.spawn("rofi -show-icons -font 'JetBrainsMonoMedium Nerd Font Mono 10' -show drun "), desc="Rofi"),
    Key([mod], "w", lazy.spawn("firefox"), desc="Firefox"),
    Key([mod], "g", lazy.spawn("geany"), desc="Geany"),
    Key([mod], "e", lazy.spawn("pcmanfm"), desc="PCManFM"),
    Key([mod], "f", lazy.spawn("filezilla"), desc="Filezilla"),
    Key([mod], "Print", lazy.spawn("flameshot gui"), desc="Flameshot"),
]

#groups = [Group(i) for i in "123456789"]

groups = [
    Group("1", layout = 'monadtall'),
    Group("2", layout = 'monadtall'),
    Group("3", layout = 'monadtall'),
    Group("4", layout = 'monadtall'),
    Group("5", layout = 'monadtall'),
    Group("6", layout = 'monadtall'),
    Group("7", layout = 'monadtall'),
    Group("8", layout = 'monadtall'),
    Group("9", layout = 'monadtall'),
    Group("0", layout = 'floating')
]


for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc = "Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc = "Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    #layout.Columns(
    #    border_focus_stack=["#d75f5f", "#8f3d3d"],
    #    border_width=3,
    #    margin=15,
    #    single_margin=0,
    #),
    #layout.Max(),
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    #layout.Matrix(),
    layout.MonadTall(
        border_width    = 3,
        border_focus    = colors['orange'],
        margin          = 15,
        ratio           = 0.50
    ),
    layout.Floating(
        border_width    = 0,
        border_focus    = colors['orange'],
    ),
    #layout.MonadWide(),
    #layout.RatioTile(),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font        = 'VictorMono Nerd Font Bold',
    #font       = 'Input Mono',
    fontsize    = 13,
    padding     = 0,
)
extension_defaults = widget_defaults.copy()

# fmt::print("{:>6}\n", i);   // align right
# fmt::print(fmt::emphasis::bold, s);
# display_format = "  {updates:>3} ",

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    padding     = 0,
                    background  = colors['dark_grey'],
                    foreground  = colors['white'],
                    fontsize    = 12,
                ),
                widget.CurrentLayout(
                    padding     = 10,
                    background  = colors['dark_grey'],
                    foreground  = colors['white'],
                    fmt         = '{:<10}',
                ),
                widget.TextBox(
                    text        = " ",
                    background  = colors['transparent'],
                    margin      = 0,
                    padding     = 0,
                ),
                widget.GroupBox(
                    #font                       = "JetBrainsMonoExtraBold Nerd Font",
                    font                        = 'VictorMono Nerd Font',
                    disable_drag                = True,
                    fontsize                    = 13,
                    highlight_method            = 'line',
                    highlight_color             = colors['dark_grey'],
                    fmt                         = "{}",
                    borderwidth                 = 0,
                    active                      = colors['true_white'],
                    #this_screen_border          = '#5294e2',
                    block_highlight_text_color  = colors['true_white'],
                    #margin_y                   = 3,
                    padding                     = 8,
                    background                  = colors['black'],
                ),
                widget.TextBox(
                    text        = " ",
                    background  = colors['transparent'],
                    foreground  = colors['black'],
                    margin      = 0,
                    padding     = 0,
                ),
                widget.CheckUpdates(
                    update_interval     = 60,
                    no_update_string    = '  0',
                    distro              = "Arch_checkupdates",
                    display_format      = "  {updates:>3} ",
                    mouse_callbacks     = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e yay')},
                    padding             = 10,
                    background          = colors['dark_grey'],
                    colour_no_updates   = colors['white'],
                    colour_have_updates = colors['orange'],
                ),
                widget.TextBox(
                    text        = " ",
                    background  = colors['transparent'],
                    foreground  = colors['black'],
                    padding     = 0,
                ),
                widget.WindowName(
                    margin      = 0,
                    padding     = 10,
                    background  = colors['transparent'],
                    foreground  = colors['white'],
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform = lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.TextBox(
                    text        = " ",
                    background  = colors['transparent'],
                    foreground  = colors['black'],
                    padding     = 0,
                ),
                widget.KeyboardLayout(
                    fmt         = '  {}',
                    padding     = 10,
                    background  = colors['dark_grey'],
                    foreground  = colors['white'],
                ),
                widget.TextBox(
                    text        = " ",
                    background  = colors['transparent'],
                    foreground  = colors['black'],
                    margin      = 0,
                    padding     = 0,
                    margin_y    = 0,
                ),
                widget.Net(
                    interface   = "enp1s0",
                    prefix      = 'M',
                    format      = '  {down} ·{up} ',
                    padding     = 10,
                    background  = colors['dark_grey'],
                    foreground  = colors['white'],
                ),
                widget.TextBox(
                    text        = " ",
                    background  = colors['transparent'],
                    foreground  = colors['black'],
                    margin      = 0,
                    padding     = 0,
                    margin_y    = 0,
                ),
                widget.CPU(
                    format      = '  {load_percent:>6.2f} %',
                    padding     = 10,
                    background  = colors['dark_grey'],
                    foreground  = colors['white'],
                ),
                widget.TextBox(
                    text        = " ",
                    background  = colors['transparent'],
                    foreground  = colors['black'],
                    margin      = 0,
                    padding     = 0,
                    margin_y    = 0,
                ),
                widget.Memory(
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                    fmt             = ' {}',
                    padding         = 10,
                    background      = colors['dark_grey'],
                    foreground      = colors['white'],
                    measure_mem     = 'G',
                    format          = '{MemUsed: 5.2f} {mm} /{MemTotal: 3.2f} {mm}',
                ),
                widget.TextBox(
                    text        = " ",
                    background  = colors['transparent'],
                    foreground  = colors['black'],
                    margin      = 0,
                    padding     = 0,
                    margin_y    = 0,
                ),
                widget.Volume(
                    update_interval = 0.1,
                    fmt             = '  {}',
                    padding         = 10,
                    background      = colors['dark_grey'],
                    foreground      = colors['white'],
                ),
                widget.TextBox(
                    text        = " ",
                    background  = colors['transparent'],
                    foreground  = colors['black'],
                    margin      = 0,
                    padding     = 0,
                    margin_y    = 0,
                ),
                widget.Clock(
                    format      = '  %a %d-%m-%Y · %H:%M:%S',
                    padding     = 10,
                    background  = colors['dark_grey'],
                    foreground  = colors['white'],
                ),
                #widget.TextBox(
                #    text       = "",
                #    background = "#00000000",
                #    foreground = "#000000",
                #    fontsize   = 20,
                #    margin     = 0,
                #    padding    = 0,
                #),
                widget.StatusNotifier(background = colors['black'],),
            ],
            24,
            background = colors['black'],
            margin          = [0, 0, 0, 0],
            border_width    =[0, 0, 5, 0],  # Draw top and bottom borders
            # border_color  = ["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder  = None
dgroups_app_rules   = []  # type: list
follow_mouse_focus  = True
bring_front_click   = False
cursor_warp         = False
floating_layout     = layout.Floating(
    float_rules = [
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class  = "confirmreset"),  # gitk
        Match(wm_class  = "galculator"),  # gitk
        Match(wm_class  = "makebranch"),  # gitk
        Match(wm_class  = "maketag"),  # gitk
        Match(wm_class  = "ssh-askpass"),  # ssh-askpass
        Match(title     = "branchdialog"),  # gitk
        Match(title     = "pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen             = True
focus_on_window_activation  = "smart"
reconfigure_screens         = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize               = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules              = None


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
