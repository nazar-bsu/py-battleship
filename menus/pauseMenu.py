from sys import stdout
from getkey import keys
import chalk


class PauseMenu:

	basic_menu_elems = ['Continue', 'Exit']

	def __init__(self, parent, menu_list=basic_menu_elems):
		self.parent = parent
		self.menu_elems = menu_list
		self.cur_item = 0
		self.need_redraw = True
		self.next = None

	def draw(self):
		stdout.write('\n')
		for (idx, menu_item) in enumerate(self.menu_elems):
			if (idx == self.cur_item):
				stdout.write(chalk.yellow(f'\t* {menu_item}\n'))
			else:
				stdout.write(f'\t {menu_item}\n')
		stdout.flush()

	def handle(self, key):
		if key == keys.ESC:
			self.next = self.parent
		elif key == keys.ENTER:
			self.menu_hanlder(self.cur_item)
		elif key == keys.UP:
			if self.cur_item != 0:
				self.cur_item -= 1
			else:
				need_redraw = False
		elif key == keys.DOWN:
			if self.cur_item != len(self.menu_elems) - 1:
				self.cur_item += 1
			else:
				need_redraw = False

	def menu_handler(index):
		if (index == 0):
				self.next = self.parent
			elif (index == 1):
				print('Thanks for the game!')
				exit(0)