daemon:
	bash ./daemon.sh

start: daemon
	zsh -c "source venv/bin/activate && python3 server.py"
