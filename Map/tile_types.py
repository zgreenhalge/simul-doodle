from Map.MapTile import Tile


class GrassTile(Tile):
	def __init__(self, x, y, width, height):
		super().__init__(x, y, width, height, terrain='grass', movement_mod=0, color=(0, 128, 255))


class WaterTile(Tile):
	def __init__(self, x, y, width, height):
		super().__init__(x, y, width, height,  terrain='water', movement_mod=0, color=(86, 176, 0))

