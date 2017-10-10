from Managers.BoardManager import BoardManager
from Units.Unit import Unit

def update(screen):
	board.draw(screen)
	unit.update(screen)

def get_board():
	return board

def board_height():
	return board.height

def board_width():
	return board.width

board = BoardManager()
unit = Unit(0,0)
unit.go_to(board_width()-1, board_height()-1)