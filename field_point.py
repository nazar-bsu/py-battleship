import chalk
from utils import TILES


class Point:
    '''
    Point with coordinates in {i,j} notation
    '''

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self):
        return '({0};{1})'.format(self.i, chr(ord('А') + self.j))

    def isHere(self, i, j):
        return i == self.i and j == self.j


class Ship:
    def __init__(self, size):
        self.size = size
        self.damage = 0

    # self.points = points
    @property
    def is_destroyed(self):
        return self.damage == self.size

    def damage(self):
        if self.damage < self.size:
            self.damage += 1


class BattlefieldPoint(Point):
    def __init__(self, i, j, ship):
        super(Point, self).__init__(i, j)
        self.touched = False
        self.ship = ship

    def getSymbol(self):
        if not self.touched:
            return TILES'[TILE_FOG_OF_WAR]'
        elif self.ship is None:
            return TILES['TILE_SEA']
        elif self.ship.is_destroyed:
            return TILES['TILE_SHIP_DESTROYED']
        else:
            return TILES['TILE_SHIP_DAMAGED']

    def touch(self):
        if not self.touched:
            self.touched = True
            if self.ship is not None:
                self.ship.damage += 1


point = BattlefieldPoint(0, 0, 'ship')
print(point.i)
print(point.j)
