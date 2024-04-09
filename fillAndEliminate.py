from printBoard import printBoard
import pygame


def fillAndEliminate(board, possibles, graph, x, y, value, eliminations, singlePossibles):
    board[x][y] = value
    for i, j in graph[(x, y)]:
        if value in possibles[i][j]:
            possibles[i][j].remove(value)
            eliminations.append(((i, j), value))
            if len(possibles[i][j]) == 1:
                [val] = possibles[i][j]
                singlePossibles.append(((i, j), val))


def fillAndEliminateGUI(board, possibles, graph, x, y, value, eliminations, singlePossibles, delayTime):
    board.model[x][y] = value
    board.cubes[x][y].set(value)
    board.cubes[x][y].draw_change(board.win, True)
    board.update_model()
    pygame.display.update()
    pygame.time.delay(delayTime)
    for i, j in graph[(x, y)]:
        if value in possibles[i][j]:
            possibles[i][j].remove(value)
            eliminations.append(((i, j), value))
            if len(possibles[i][j]) == 1:
                [val] = possibles[i][j]
                singlePossibles.append(((i, j), val))
