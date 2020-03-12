from getkey import getkey, keys
from utils import *
from field_point import *
pointer = Point(0,0)
N = 10

field = [[0] * N for i in range(N)]
for i in range(0,10):
	for j in range(0,10):
		field[i][j] = FieldPoint(i,j,None)

def draw_field():
	print('  ',end='')
	for c in char_range('А', chr(ord('А') + N - 1)):
		print('', c,end=' ')
	print('')
	for i in range(0,N):
		print(i, end=' ')
		for j in range(0,N):
			if (i == pointer.y and j == pointer.x):
				print('[',field[i][j].getSymbol(),']',sep='', end='')
			else:
				print('',field[i][j].getSymbol(), end=' ')
		print('')
	print('Current position:', pointer)

while True:
	clear_screen()
	draw_field()
	key = getkey()
	if key == keys.ESC:
		print('Thanks for the game!')
		exit(0)
	elif key == keys.ENTER:
		print('ENTER') 
	elif key == keys.UP:
		pointer.y-=1
	elif key == keys.DOWN:
		pointer.y+=1
	elif key == keys.LEFT:
		pointer.x-=1
	elif key == keys.RIGHT:
		pointer.x+=1
	elif key == keys.SPACE:
		field[pointer.y][pointer.x].touch()
	# elif key == keys.CTRL_A:
	# 	print(pointer) 
	elif key == 'c':
		clear_screen()
	else:
		print(key)
		
