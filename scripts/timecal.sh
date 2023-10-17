pid=$(ps -C gsimplecal -o pid=)
if [ -n "$pid" ]; then
	kill $(ps -C gsimplecal -o pid=)
else
	exec gsimplecal
fi
