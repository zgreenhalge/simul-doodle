import pygame


# class MapTile:
# 	tile_width = tile_height = 50
#
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
#
# 	def get_x():
# 		return self.x
#
# 	def get_y():
# 		return self.y
#
# 	def get_height(self):
# 		return tile_height
#
# 	def get_width(self):
# 		return tile_width
#
# 	def get_type(self):
# 		return self.tile_type
#
# 	def get_move_mod(self):
# 		return self.movement_mod
#
# 	def get_color(self):
# 		return self.color
#
# 	def draw(self, screen):
# 		pygame.draw.rect(screen, self.get_color(), self.get_rectangle())
#
# 	def get_rectangle(self):
# 		width = MapTile.tile_width
# 		height = MapTile.tile_height
# 		return pygame.Rect(self.x * width, self.y * height, width, height)


class Tile:
	def __init__(self, x, y, width, height, terrain, movement_mod, color):
		self.rect = pygame.Rect(x, y, width, height)
		self.terrain = terrain
		self.movement_mod = movement_mod
		self.color = color

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)