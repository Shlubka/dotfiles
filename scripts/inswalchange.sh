#!/bin/sh

file=$(find ~/.wallpaper/ -type f | shuf -n1)
echo preload = $file> ~/.config/hypr/hyprpaper.conf
echo wallpaper = LVDS-1,$file>> ~/.config/hypr/hyprpaper.conf
wal -i $file
pywalfox update
python ~/.config/scripts/work-color.py
makoctl reload
killall hyprpaper
hyprpaper &
killall waybar
waybar &
sleep 10m
