def update(screen, board, unit):
	board.draw(screen)
	unit.update(screen, board)
	unit.go_to(board, board.width - 1, board.height - 1)

