from field_point import Point, FieldPoint, Ship
from getkey import getkey, keys
from utils import char_range
from PauseMenu import PauseMenu



class Battleship:

	def __init__(self):
		
		self.next = None
		self.need_redraw = True
		self.pause_menu = PauseMenu(self)
		self.pointer = Point(0, 0)
		self.N = 10
		self.log = ''
		self.field = [[0] * self.N for i in range(self.N)]
		for i in range(0, 10):
			for j in range(0, 10):
				ship = None
				if i % 2 == 1 and j % 2 == 1:
					ship = Ship(1)
				self.field[i][j] = FieldPoint(i, j, ship)

		self.SHIPS = [[Ship(5-i)] * i for i in range(1, 5)]

	def draw(self):
		print('  ', end='', flush=False)
		for c in char_range('А', chr(ord('А') + self.N - 1)):
			print('', c, end=' ', flush=False)
		print('', flush=False)
		for i in range(0, self.N):
			print(i, end=' ', flush=False)
			for j in range(0, self.N):
				if i == self.pointer.i and j == self.pointer.j:
					print('[', self.field[i][j].getSymbol(), ']',
						sep='', end='', flush=False)
				else:
					print('', self.field[i][j].getSymbol(), end=' ', flush=False)
			print('')
		print('Current position:', self.pointer, flush=False)
		print('Log:', self.log, flush=True)

	def handle(self, key):
		if key == keys.ESC:
			self.next = self.pause_menu
		elif key == keys.ENTER:
			print('ENTER')
		elif key == keys.UP:
			if self.pointer.i != 0:
				self.pointer.i -= 1
			else:
				need_redraw = False
		elif key == keys.DOWN:
			if self.pointer.i != self.N - 1:
				self.pointer.i += 1
			else:
				need_redraw = False
		elif key == keys.LEFT:
			if self.pointer.j != 0:
				self.pointer.j -= 1
			else:
				need_redraw = False
		elif key == keys.RIGHT:
			if self.pointer.j != self.N - 1:
				self.pointer.j += 1
			else:
				need_redraw = False
		elif key == keys.SPACE:
			self.field[self.pointer.i][self.pointer.j].touch()
			self.log = 'Touched point ' + str(self.pointer)
		elif key == 'c':
			clear_screen()
		else:
			print(key)
