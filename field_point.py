TILE_SHIP_DAMAGED = '#'
TILE_SHIP_DESTROYED = '*'
TILE_SEA = '~'
TILE_FOG_OF_WAR = '▢'
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = x
	def __str__(self):
	 return '({0};{1})'.format(self.x,self.y)
class Ship:
	def __init__(self, size, points):
		self.size = x
		self.damaged = 0
		self.points = points		
	def isDestroyd(self):
		if (self.damaged == self.size):
			return True
		else:
			return False

class FieldPoint(Point):
	def __init__(self, x, y, ship):
		super(FieldPoint, self).__init__(x,y)
		self.touched = False
		self.ship = ship
	def getSymbol(self):
		print('test')
point = FieldPoint(0,0, 'ship')
print(point.x)
print(point.y)