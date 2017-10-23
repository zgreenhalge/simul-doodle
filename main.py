import pygame
from pygame.locals import *

from Managers import GameManager
from Managers.event_handlers import handle_keys
from Map.game_map import GameMap
from Units.Unit import Unit

# import game

if __name__ == '__main__':
	# SETTINGS
	pygame.init()
	pygame.display.set_caption("Ayy Lmao")
	screen = pygame.display.set_mode([500, 500], RESIZABLE)
	clock = pygame.time.Clock()
	done = False
	ticks = 0

	# MAP AND UNIT INITIALIZE
	unit = Unit(0, 0)
	game_map = GameMap()

	# while ticks < 100 and not done:
	while not done:
		for event in pygame.event.get():
			quit = handle_keys(event).get('quit')
			resize = handle_keys(event).get('resize')
			mmb_down = handle_keys(event).get('mmb_down')
			mmb_drag = handle_keys(event).get('mmb_drag')

			if quit:
				done = True
			if resize:
				screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
			if mmb_down:
				# These can be used elsewhere as long as the button is held
				x0 = event.pos[0]
				y0 = event.pos[1]
			if mmb_drag:
				xf = event.pos[0]
				yf = event.pos[1]
				print("A rectangle with sides {} and {}".format(abs(xf - x0), abs(yf - y0)))

		pygame.display.update()  # No args: same as flip
		ticks += 1
		if ticks % 10 == 0:
			GameManager.update(screen, game_map, unit)
			print(ticks)
		clock.tick(60)  # TODO make this scale w user selected speed somehow
