from field_point import Point, BattlefieldPoint, Ship
from getkey import getkey, keys
from utils import char_range
from PauseMenu import PauseMenu

from sys import stdout


class BattleshipState:

    EMPTY_FIELD = [[0] * 10 for i in range(10)]

    def __init__(self, field=EMPTY_FIELD):

        self.next = None
        self.need_redraw = True
        self.pause_menu = PauseMenu(self)
        self.pointer = Point(0, 0)
        self.N = 10
        self.log = ''
        self.field = field
        for i in range(0, 10):
            for j in range(0, 10):
                ship = None
                if i % 2 == 1 and j % 2 == 1:
                    ship = Ship(1)
                self.field[i][j] = BattlefieldPoint(i, j, ship)

        # self.SHIPS = [[Ship(5-i)] * i for i in range(1, 5)]

    def draw(self):
        stdout.write('  ')
        for c in char_range('А', chr(ord('А') + self.N - 1)):
            stdout.write(f' {c} ')
        stdout.write('\n')
        for i in range(0, self.N):
            stdout.write(f'{i} ')
            for j in range(0, self.N):
                if (self.pointer.isHere(i, j)):
                    stdout.write(f'[{self.field[i][j].getSymbol()}]')
                else:
                    stdout.write(f' {self.field[i][j].getSymbol()} ')
            stdout.write('\n')
        stdout.write(f'Current position: {str(self.pointer)}\n')
        stdout.write(f'Log: {self.log}')
        stdout.flush()

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
