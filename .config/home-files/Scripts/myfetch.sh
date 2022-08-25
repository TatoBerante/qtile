#!/bin/sh

URED="\e[4;31m"
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[34m"
MAGENTA="\e[35m"
CYAN="\e[36m"
LGRAY="\e[37m"
LRED="\e[91m"
LGREEN="\e[92m"
LYELLOW="\e[93m"
LBLUE="\e[94m"
LMAGENTA="\e[95m"
LCYAN="\e[96m"
WHITE="\e[97m"
ENDCOLOR="\e[0m"

RAM="$(free -h | awk '/^Mem:/ {print $3 "/" $2}')"
GPU="$(glxinfo -B | grep Device: | sed "s/([^)]*)/()/g" | sed 's/[)(]//g' | xargs | cut -d ' ' -f2-)"
DESKTOP="${XDG_CURRENT_DESKTOP}"

if [ -z "${WM}" ]; then
	if [ "${XDG_CURRENT_DESKTOP}" ]; then
		ENVTYPE='Desktop'
		WM="${XDG_CURRENT_DESKTOP}"
	elif [ "${DESKTOP_SESSION}" ]; then
		ENVTYPE='Desktop'
		WM="${DESKTOP_SESSION}"
	else
		ENVTYPE='WM'
		WM="$(tail -n 1 "${HOME}/.xinitrc" | cut -d ' ' -f 2)"
	fi
else
	ENVTYPE='WM'

fi

#$ENVTYPE: $WM 

echo -e "${BLUE}"`hostnamectl | grep 'Operating System' | cut -d ' ' -f3-`" :: Kernel "`uname -r`"${ENDCOLOR}"
echo -e "${LGRAY}"`awk -F':' '/^model name/ {print $2}' /proc/cpuinfo | uniq | sed -e 's/^[ \t]*//'`" (`cat /proc/stat | awk '/cpu/{printf("%.2f%\n"), ($2+$4)*100/($2+$4+$5)}' |  awk '{print $0}' | head -1`)${ENDCOLOR}"
echo -e "${LGRAY}${GPU}"
echo -e "${LGRAY}"`cat /sys/devices/virtual/dmi/id/board_name`" ("`cat /sys/class/dmi/id/sys_vendor`")${ENDCOLOR}"
echo -e "${LGRAY}RAM USAGE: "`free | awk '/Mem/{printf("%.2f%"), $3/$2*100}'`" (${RAM})${ENDCOLOR}"
echo -e "${LMAGENTA}${ENVTYPE} -> ${WM} ${ENDCOLOR}"
echo ""
echo -e "${RED}${ENDCOLOR} ${LRED}${ENDCOLOR} ${GREEN}${ENDCOLOR} ${LGREEN}${ENDCOLOR} ${YELLOW}${ENDCOLOR} ${LYELLOW}${ENDCOLOR} ${BLUE}${ENDCOLOR} ${LBLUE}${ENDCOLOR} ${MAGENTA}${ENDCOLOR} ${LMAGENTA}${ENDCOLOR} ${CYAN}${ENDCOLOR} ${LCYAN}${ENDCOLOR} ${LGRAY}${ENDCOLOR} ${WHITE}${ENDCOLOR}"
#echo "\e[1;31m\e[0m\e[1;91m\e[0m \e[1;32m\e[0m\e[1;92m\e[0m \e[1;33m\e[0m\e[1;93m\e[0m \e[1;34m\e[0m\e[1;94m\e[0m \e[1;35m\e[0m\e[1;95m\e[0m \e[1;36m\e[0m\e[1;96m\e[0m \e[1;37m\e[0m\e[1;97m\e[0m"
echo ""
echo ""
