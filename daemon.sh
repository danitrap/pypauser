#!/bin/bash

if ps aux | grep -v grep | grep ydotool >/dev/null; then
	# do nothing
	echo "ydotool is already running"
else
	# start ydotool
	sudo -b ydotoold --socket-path="$HOME/.ydotool_socket" --socket-own="$(id -u):$(id -g)"
fi
