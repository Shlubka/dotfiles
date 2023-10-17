pid=$(ps -C wofi -o pid=)
if [ -n "$pid" ]; then
	kill wofi
else
	bash ~/.config/scripts/powermenu.sh
fi
