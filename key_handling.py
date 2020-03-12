from getkey import getkey, keys

while True:
	key = getkey()
	if key == keys.SPACE:
		print('SPACE')
	elif key == keys.ENTER:
		print('ENTER') 
	elif key == keys.UP:
		print('UP') 
	elif key == keys.DOWN:
		print('DOWN') 
	elif key == keys.LEFT:
		print('LEFT') 
	elif key == keys.RIGHT:
		print('RIGHT') 