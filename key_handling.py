from platform import system    # For getting the operating system name
from subprocess  import call# For executing a shell command

def clear_screen():
    """
    Clears the terminal screen.
    """
    # Clear command as function of OS
    command = "cls" if system().lower()=="windows" else "clear"

    # Action
    return call(command) == 0
from getkey import getkey, keys
cur_pint = {
	'x':0,
	'y':0
}
def draw_field():
	for i in range(0,10):
		for j in range(0,10):
			if (i == cur_pint['y'] and j == cur_pint['x']):
				print('0', end='')
			else:
				print('~', end='')
		print('')
	print(cur_pint)
while True:
	clear_screen()
	draw_field()
	key = getkey()
	if key == keys.SPACE:
		print('SPACE')
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
		
