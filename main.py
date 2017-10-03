import pygame, sys
from Map.MapManager import MapManager
from pygame.locals import *
# import game

if __name__ == '__main__':
	pygame.init()
	pygame.display.set_caption("Ayy Lmao")
	screen = pygame.display.set_mode([500, 500], RESIZABLE)
	clock = pygame.time.Clock()
	done = False
	map = MapManager()

	while not done:
		for event in pygame.event.get():
			if event.type == QUIT:
				done = True
			if event.type == VIDEORESIZE:
				screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
			# TODO on middle mouse down, capture position; on middle mouse up, drag difference between two positions

		map.draw(screen)
		pygame.display.flip()
		clock.tick(60) # TODO make this scale w user selected speed somehow