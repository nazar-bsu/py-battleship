from getkey import keys
import chalk


class State:

    def __init__(self):
        self.need_redraw = True
        self.next = None

    def draw(self):
        pass

    def handle(self, key):
        pass
