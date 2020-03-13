from getkey import getkey, keys
from utils import *
from field_point import *
pointer = Point(0,0)
N = 10
log=''
field = [[0] * N for i in range(N)]
for i in range(0,10):
	for j in range(0,10):
		ship = None
		if( i%2 == 1 and j%2 == 1):
			ship = Ship(1)
		field[i][j] = FieldPoint(i,j,ship)
		# field[i][j].touched = True

def draw_field():
	print('  ',end='', flush = False)
	for c in char_range('А', chr(ord('А') + N - 1)):
		print('', c,end=' ', flush = False)
	print('', flush = False)
	for i in range(0,N):
		print(i, end=' ', flush = False)
		for j in range(0,N):
			if (i == pointer.i and j == pointer.j):
				print('[',field[i][j].getSymbol(),']',sep='', end='', flush = False)
			else:
				print('',field[i][j].getSymbol(), end=' ', flush = False)
		print('')
	print('Current position:', pointer, flush = False)
	print('Log:', log, flush = True)
need_redraw=True
while True:
	if(need_redraw):
		clear_screen()
		draw_field()
	else:
		need_redraw=True
	key = getkey()
	if key == keys.ESC:
		print('Thanks for the game!')
		exit(0)
	elif key == keys.ENTER:
		print('ENTER') 
	elif key == keys.UP:
		if (pointer.i != 0):
			pointer.i-=1
		else:
			need_redraw=False
	elif key == keys.DOWN:
		if (pointer.i != N -1):
			pointer.i+=1
		else:
			need_redraw=False
	elif key == keys.LEFT:
		if (pointer.j != 0):
			pointer.j-=1
		else:
			need_redraw=False
	elif key == keys.RIGHT:
		if (pointer.j != N -1):
			pointer.j+=1
		else:
			need_redraw=False
	elif key == keys.SPACE:
		field[pointer.i][pointer.j].touch()
		log = 'Touched point ' + str(pointer)
	elif key == 'c':
		clear_screen()
	else:
		print(key)
		
