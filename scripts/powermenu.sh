#!/bin/bash

entries="⏻ Shutdown\n⭮ Reboot\n⇠ Logout"

selected=$(echo -e $entries|wofi  -b  --width 10 --height 180 --dmenu --cache-file /dev/null -x 1159 -y 1 | awk '{print tolower($2)}')

case $selected in
  logout)
    killall Hyprland;;
  reboot)
    exec systemctl reboot;;
  shutdown)
    exec poweroff -i;;
esac
