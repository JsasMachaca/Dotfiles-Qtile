#neofetch
#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias tree="tree -C"
alias cat='bat'
alias ls='lsd -U'
# alias ranger='ranger ~'
# alias cd='ranger'
# alias clear='clear && neofetch'

PS1='\[\e[0;38;5;221m\]\u\[\e[0;38;5;159m\]@\[\e[0;38;5;105m\]\H\[\e[0m\]:\[\e[0;38;5;30m\]\w \[\e[0;1;38;5;159m\] \[\e[0m\]'

function ChangeMod(){
	chmod +x $1	
}

function Apagar(){
	shutdown now
}

function DuplicateScreens(){
	xrandr --output eDP-1 --mode 1920x1080 --output HDMI-1 --mode 1920x1080 --same-as eDP-1
}

function Tecsup(){
	ranger ~/Desktop/Tecsup/
}

function Mysql {
	systemctl start mysql
}

function Mongodb {
	systemctl start mongodb
}

export PATH="$PATH:$HOME/.config/composer/vendor/bin"
export PATH="$PATH:/home/jisas/.local/bin"
export ORACLE_HOME="/usr/lib/oracle/VERSION/client64"
export LD_LIBRARY_PATH="$ORACLE_HOME/lib"
export PATH="$PATH:$ORACLE_HOME/bin"
