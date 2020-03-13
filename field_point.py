TILE_SHIP_DAMAGED = '*'
TILE_SHIP_DESTROYED = '#'
TILE_SEA = '~'
TILE_FOG_OF_WAR = '▢'
class Point:
	'''
	Point with coordinates in {i,j} notation
	'''
	def __init__(self, i, j):
		self.i = i
		self.j = j
	def __str__(self):
	 return '({0};{1})'.format(self.i,chr(ord('А') + self.j))
class Ship:
	def __init__(self, size):
		self.size = size
		self.damage = 0
		# self.points = points		
	@property
	def isDestroyd(self):
		return self.damage == self.size
	def demage(self):
		if (self.damage < self.size):
			self.damage+=1
		

class FieldPoint(Point):
	def __init__(self, i, j, ship):
		super(FieldPoint, self).__init__(i,j)
		self.touched = False
		self.ship = ship
	def getSymbol(self):
		if (not self.touched):
			return TILE_FOG_OF_WAR
		elif (self.ship == None):
			return TILE_SEA
		elif (self.ship.isDestroyd):
			return TILE_SHIP_DESTROYED
		else:
			return TILE_SHIP_DAMAGED
	

	def touch(self):
		if (not self.touched):
			self.touched = True
			if (self.ship != None):
				self.ship.damage += 1
point = FieldPoint(0,0, 'ship')
print(point.i)
print(point.j)