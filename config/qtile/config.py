from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from os import path
import subprocess


@hook.subscribe.startup_once
def startup_once():
    home = path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
  
mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.

    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Resise MonadTall
    Key([mod, "control"], "left", lazy.layout.grow()),
    Key([mod, "control"], "right", lazy.layout.shrink()),

    Key([mod], "s", lazy.window.toggle_floating()),
    #Key([mod], "t", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    #                CUSTOM KEYS

        # Rofi
    Key([mod], "d", lazy.spawn("rofi -show drun")),

        # Audio Control
    Key([], "XF86AudioLowerVolume", lazy.spawn(
            "pactl set-sink-volume @DEFAULT_SINK@ -5%"
        )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
            "pactl set-sink-volume @DEFAULT_SINK@ +5%"
        )),
    Key([], "XF86AudioMute", lazy.spawn(
            "pactl set-sink-mute @DEFAULT_SINK@ toggle"
        )),

        # Brightness Control
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

        # Screenshots
    Key([mod, "shift"], "s", lazy.spawn("scrot -e 'xclip -selection clipboard -t image/png -i $f'")),
]

#               GROUPS 

groups = [Group(i) for i in ["   ", "   ", " 󰨞  ", "   ", "   ", "   ",]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name, switch_group=True)),
        Key([mod, "control"], actual_key, lazy.window.togroup(group.name, switch_group=False)),
    ])


layouts = [
    layout.MonadTall(border_focus_stack=["#0f101a", "#0f101a"], border_focus=["#5D5D5D", "#5D5D5D"], border_width=1, margin=5),
    layout.MonadWide(border_focus_stack=["#0f101a", "#0f101a"], border_focus=["#5D5D5D", "#5D5D5D"], border_width=1, margin=5),
    # layout.Columns(border_focus_stack=["#0f101a", "#0f101a"], border_focus=["#5D5D5D", "#5D5D5D"], border_width=1, margin=5),
    layout.Max(border_focus_stack=["#0f101a", "#0f101a"], border_focus=["#5D5D5D", "#5D5D5D"], border_width=1, margin=2),
]

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
#       WIDGETS ARCH LOGO    .
                widget.TextBox(
                    text='   ',
                    foreground=["#FF0055", "#FF0055"],
                    background=["#0f101a", "#0f101a"],
                    fontsize=22,
                ),

                widget.Sep(
                    foreground=["f1ffff", "#f1ffff"],
                ),

                widget.Spacer(
                    length=20,
                    background=["#0f101a", "#0f101a"],
                ),


#       WIDGETS GROUPS     .
                widget.GroupBox(
                    foreground=["#f1ffff", "#f1ffff"],
                    background  =["#0f101a", "#0f101a"],
                    font='UbuntuMono Nerd Font',
                    fontsize=20,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#f1ffff", "#f1ffff"],
                    inactive=["#525050", "#525050"],
                    rounded=False,
                    highlight_method='block',
                    this_current_screen_border=["#F07178", "#F07178"],
                    this_screen_border=["#5c5c5c", "#5c5c5c"],
                    other_current_screen_border=["#0f101a", "#0f101a"],
                    other_screen_border=["#0f101a", "#0f101a"],
                ),

                widget.WindowName(
                    foreground=["#F07178", "#F07178"],
                    background=["#0f101a", "#0f101a"],
                ),

                widget.Sep(
                    background=["#0f101a", "#0f101a"],
                    foreground=["#0f101a", "#0f101a"],
                ),


#                                   WIDGETS RIGHT BAR                 .

#       WIDGETS UPDATES     .
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'bars', 'bar05.png'),
                ),

                widget.TextBox(
                    text=" ",
                    foreground=["0f101a", "0f101a"],
                    background=["#ffd47e", "#ffd47e"],
                ),

                widget.CheckUpdates(
                    background=["#ffd47e", "#ffd47e"],
                    foreground=["#000000", "#000000"],
                    display_format='{updates}',
                    no_update_string='0',
                    colour_have_updates=["0f101a", "0f101a"],
                    colour_no_updates=["0f101a", "0f101a"],
                    custom_command='checkupdates',
                    update_interval=2400,
                ),


#       WIDGETS NETWORK   .
                 widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'bars', 'bar04.png'),
                ),

                widget.TextBox(
                    text=' ',
                    foreground=["#0f101a", "#0f101a"],
                    background=["#F07178", "#F07178"],
                ),

                widget.Net(
                    interface="wlp0s20f3",
                    format="{interface} :{down} ↓",
                    foreground=["#0f101a", "#0f101a"],
                    background=["#F07178", "#F07178"],
                ),

                widget.Sep(
                    foreground=["#F07178", "#F07178"],
                    background=["#F07178", "#F07178"],
                ),


#       WIDGETS LAYOUT    .
                 widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'bars', 'bar01.png'),
                ),

                widget.CurrentLayoutIcon(
                    background=["#FF0055", "#FF0055"],
                    scale = 0.6,
                ),

                widget.CurrentLayout(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#FF0055", "#FF0055"],
                ),


#       WIDGETS CLOCK   . 
                 widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'bars', 'bar02.png'),
                ),

                widget.TextBox(
                    text='󰃰 ',
                    foreground=["#000000", "#000000"],
                    background=["#B900FF", "#B900FF"],
                    # background=["#033681", "#033681"],
                ),

                widget.Clock(
                    foreground=["#000000", "#000000"],
                    background=["#B900FF", "#B900FF"],
                    # background=["#033681", "#033681"], # second color ["#B900FF"]
                    format="%d/%m/%Y ",
                ),

                widget.Sep(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#B900FF", "#B900FF"],
                    # background=["#033681", "#033681"],
                ),

                widget.Clock(
                    foreground=["#000000", "#000000"],
                    background=["#B900FF", "#B900FF"],
                    # background=["#033681", "#033681"],
                    format=" %I:%M %p",
                ),

                widget.Sep(
                    # background=["#033681", "#033681"],
                    # foreground=["#033681", "#033681"],
                    background=["#B900FF", "#B900FF"],
                    foreground=["#B900FF", "#B900FF"],
                ),


#       WIDGETS SYSTRAY   
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'bars', 'bar03.png'),
                ),

                widget.Sep(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#0f101a", "#0f101a"],
                ),
                
                widget.Systray(
                    foreground=["#F07178", "#F07178"],
                    background=["#0f101a", "#0f101a"],
                ),
            ],
            21,
            opacity=0.94
        ),
    ),
]

# Drag floating layouts.

# Reglas y configuraciones de las pantallas flotantes   .
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
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
        Match(wm_class="Pavucontrol"), # Pantalla de control de audio
        Match(wm_class="Lightdm-gtk-greeter-settings"), # Configuración de Lightdm
        Match(wm_class="Lxappearance"), # Configuración de temas
        Match(title="wificonection"),
        Match(title="Preferencias de Terminator"),
        Match(wm_class="feh"),
        Match(wm_class="Matplotlib"),
    ],
    border_focus="#0f101a",
    border_width=1,
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
