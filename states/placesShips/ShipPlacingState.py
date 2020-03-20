from field_point import Point, BattlefieldPoint, Ship
from getkey import getkey, keys
from utils import char_range, TILES
from PauseMenu import PauseMenu

from sys import stdout


class ShipPlacinState:

    sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    SHIPS = [Ship(size) for size in sizes]

    def getShipBorders():
        pass

    def __init__(self, ships=SHIPS, N=10):

        self.next = None
        self.need_redraw = True
        self.pause_menu = PauseMenu(self)

        self.ships = ships
        self.N = N
        self.log = ''
        self.field = [[TILES['TILE_SEA']] * self.N for _ in range(self.N)]
        self.cur_ship = ships[0]
        self.cur_points = []
        for j in self.cur_ship.size:
            self.cur_points += Point(0, j)

    def draw(self):
        # stdout.write('  ')
        # for c in char_range('А', chr(ord('А') + self.N - 1)):
        # 	stdout.write(f' {c} ')
        # stdout.write('\n')
        # for i in range(0, self.N):
        # 	stdout.write(str(i) + ' ')
        # 	for j in range(0, self.N):
        # 		if i == self.pointer.i and j == self.pointer.j:
        # 			stdout.write(f'[{self.field[i][j].getSymbol()}]')
        # 		else:
        # 			stdout.write(f' {self.field[i][j].getSymbol()} ')
        # 	stdout.write('\n')
        # stdout.write(f'Current position: {str(self.pointer)}\n')
        # stdout.write(f'Log: {self.log}')
        # stdout.flush()

    def handle(self, key):
        if key == keys.ESC:
            self.next = self.pause_menu
        elif key == keys.ENTER:
            pass
            # PLACE SHIP
            # ships.pop(cur_ship_index)
            # clear old self.cur_points.clear()
            # generate next point
            # place them on field
            #
            # draw??
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
# sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
# SHIPS = [Ship(size) for size in sizes]
# print([ship.size for ship in SHIPS])
