import chalk
TILES = dict(
	TILE_SHIP_DAMAGED = chalk.yellow('*'),
	TILE_SHIP_DESTROYED = chalk.red('#'),
	TILE_SEA = chalk.blue('~'),
	TILE_FOG_OF_WAR = '▢'
)

print(TILES['TILE_SHIP_DAMAGED'])