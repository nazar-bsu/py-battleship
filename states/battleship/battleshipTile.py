from utils import TILES
from ship import Ship
class BattleshipTile:
	def __init__(self, ship: Ship, touched = False):
		self.touched = touched
		self.ship = ship

	'''
	Point with coordinates in {i,j} notation
	'''
	def getSymbol(self) -> str:
		if not self.touched:
			return TILES['TILE_FOG_OF_WAR']
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