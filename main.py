from config import start_state
from getkey import getkey
from utils import clear_screen


def main():
	cur_state = start_state
	while True:
		if (cur_state.need_redraw):
			clear_screen()
			cur_state.draw()
		else:
			need_redraw = True

		cur_state.handle(getkey())

		if (cur_state.next):
			prev_state = cur_state
			cur_state = cur_state.next
			prev_state.next = None

if __name__ == "__main__":
	main()
