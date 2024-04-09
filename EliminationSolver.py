from fillAndEliminate import fillAndEliminate, fillAndEliminateGUI
from collections import deque
from nextFreeBlock import findNextFreeBlock
from initializeGraph import initializeGraph
import pygame


def eliminationSolverHelper(board, possibles, graph, x, y):
    if x is None:
        return True
    currentList = list(possibles[x][y])
    possibles[x][y] = set()
    for value in currentList:
        completed = True
        singlePossibles = deque()
        eliminations = []
        fillAndEliminate(board, possibles, graph, x, y, value, eliminations, singlePossibles)
        fills = [((x, y), value)]
        while singlePossibles:
            (i, j), val = singlePossibles.popleft()
            if board[i][j] == 0 and val not in possibles[i][j]:
                completed = False
                break
            possibles[i][j].remove(val)
            fills.append(((i, j), val))
            eliminations.append(((i, j), val))
            fillAndEliminate(board, possibles, graph, i, j, val, eliminations, singlePossibles)
        if completed:
            i, j = findNextFreeBlock(board, x, y)
            if eliminationSolverHelper(board, possibles, graph, i, j):
                return True
        for (i, j), val in eliminations:
            possibles[i][j].add(val)
        for (i, j), val in fills:
            board[i][j] = 0
    possibles[x][y] = set(currentList)
    return False


def initialSolver(board, possibles, graph):
    singlePossibles = deque()
    eliminations = []
    for i in range(9):
        for j in range(9):
            if len(possibles[i][j]) == 1:
                [value] = possibles[i][j]
                singlePossibles.append(((i, j), value))
    while singlePossibles:
        (i, j), value = singlePossibles.popleft()
        possibles[i][j].remove(value)
        fillAndEliminate(board, possibles, graph, i, j, value, eliminations, singlePossibles)


def eliminationSolverHelperGUI(board, possibles, graph, x, y, delayTime):
    if x is None:
        return True
    currentList = list(possibles[x][y])
    possibles[x][y] = set()
    for value in currentList:
        completed = True
        singlePossibles = deque()
        eliminations = []
        fillAndEliminateGUI(board, possibles, graph, x, y, value, eliminations, singlePossibles, delayTime)
        fills = [((x, y), value)]
        while singlePossibles:
            (i, j), val = singlePossibles.popleft()
            if board.model[i][j] == 0 and val not in possibles[i][j]:
                completed = False
                break
            possibles[i][j].remove(val)
            fills.append(((i, j), val))
            eliminations.append(((i, j), val))
            fillAndEliminateGUI(board, possibles, graph, i, j, val, eliminations, singlePossibles, delayTime)
        if completed:
            i, j = findNextFreeBlock(board.model, x, y)
            if eliminationSolverHelperGUI(board, possibles, graph, i, j, delayTime):
                return True
        for (i, j), val in eliminations:
            possibles[i][j].add(val)
        for (i, j), val in fills:
            board.model[i][j] = 0
            board.cubes[i][j].set(0)
            board.update_model()
            board.cubes[i][j].draw_change(board.win, False)
            pygame.display.update()
            pygame.time.delay(delayTime)
    possibles[x][y] = set(currentList)
    return False


def initialSolverGUI(board, possibles, graph, delayTime):
    singlePossibles = deque()
    eliminations = []
    for i in range(9):
        for j in range(9):
            if len(possibles[i][j]) == 1:
                [value] = possibles[i][j]
                singlePossibles.append(((i, j), value))
    while singlePossibles:
        (i, j), value = singlePossibles.popleft()
        possibles[i][j].remove(value)
        fillAndEliminateGUI(board, possibles, graph, i, j, value, eliminations, singlePossibles, delayTime)


def eliminationSolverGUI(board, delayTime):
    graph = initializeGraph()
    possibles = findPossibles(board.model)
    initialSolverGUI(board, possibles, graph, delayTime)
    i, j = findNextFreeBlock(board.model, 0, 0)
    eliminationSolverHelperGUI(board, possibles, graph, i, j, delayTime)


def findPossibles(board):
    fullSet = set(range(1, 10))
    possibles = [None] * 9
    for i in range(9):
        possibles[i] = [None] * 9
        for j in range(9):
            if board[i][j] == 0:
                possibles[i][j] = fullSet.copy()
            else:
                possibles[i][j] = set()
    for i, row in enumerate(board):
        taken = set(row)
        for j in range(9):
            possibles[i][j] -= taken
    for j in range(9):
        taken = set()
        for i in range(9):
            taken.add(board[i][j])
        for i in range(9):
            possibles[i][j] -= taken
    for i in range(3):
        for j in range(3):
            taken = set()
            top = i * 3
            left = j * 3
            for k in range(top, top + 3):
                for l in range(left, left + 3):
                    taken.add(board[k][l])
            for k in range(top, top + 3):
                for l in range(left, left + 3):
                    possibles[k][l] -= taken
    return possibles
