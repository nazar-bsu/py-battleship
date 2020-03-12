from getkey import getkey, keys
from utils import *
from field_point import *
cur_point = Point(0,0)
def draw_field():
	print('  ',end='')
	for c in char_range('А', 'Й'):
		print('', c,end=' ')
	print('')
	for i in range(0,10):
		print(i, end=' ')
		for j in range(0,10):
			if (i == cur_point.y and j == cur_point.x):
				print('[~]', end='')
			else:
				print('',TILE_FOG_OF_WAR, end=' ')
		print('')
	print('Current position:', cur_point)

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
		cur_point.y-=1
	elif key == keys.DOWN:
		cur_point.y+=1
	elif key == keys.LEFT:
		cur_point.x-=1
	elif key == keys.RIGHT:
		cur_point.x+=1
	# elif key == keys.CTRL_A:
	# 	print(cur_point) 
	elif key == 'c':
		clear_screen()
	else:
		print(key)
		
