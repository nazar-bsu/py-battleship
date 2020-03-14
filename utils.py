from platform import system    # For getting the operating system name
from subprocess  import call# For executing a shell command
def clear_screen():
	"""
	Clears the terminal screen.
	"""
	# Clear command as function of OS
	command = "cls" if system().lower()=="windows" else "clear"
	# Action
	return call(command, shell=True) == 0

def char_range(c1, c2):
	"""Generates the characters from `c1` to `c2`, inclusive."""
	for c in range(ord(c1), ord(c2)+1):
		yield chr(c)
