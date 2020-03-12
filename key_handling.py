from getkey import getkey, keys
from platform import system    # For getting the operating system name
from subprocess  import call# For executing a shell command
def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)
def clear_screen():
    """
    Clears the terminal screen.
    """
    # Clear command as function of OS
    command = "cls" if system().lower()=="windows" else "clear"

    # Action
    return call(command) == 0
cur_pint = {
	'x':0,
	'y':0
}
def draw_field():
	print('  ',end='')
	for c in char_range('А', 'Й'):
		print(c, end=' ')
	print('')
	for i in range(0,10):
		print(i, end=' ')
		for j in range(0,10):
			if (i == cur_pint['y'] and j == cur_pint['x']):
				print('0', end=' ')
			else:
				print('~', end=' ')
		print('')
	print(cur_pint)
while True:
	clear_screen()
	draw_field()
	key = getkey()
	if key == keys.ESC:
		exit(0)
	elif key == keys.ENTER:
		print('ENTER') 
	elif key == keys.UP:
		cur_pint['y']-=1
	elif key == keys.DOWN:
		cur_pint['y']+=1
	elif key == keys.LEFT:
		cur_pint['x']-=1
	elif key == keys.RIGHT:
		cur_pint['x']+=1
	elif key == keys.CTRL_A:
		print(cur_pint) 
	elif key == 'c':
		clear_screen()
	else:
		print(key)
		
