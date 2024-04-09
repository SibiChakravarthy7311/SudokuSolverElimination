from check import check
from nextFreeBlock import findNextFreeBlock


def bruteForceSolverHelper(board, x, y):
    if x is None:
        return True
    for val in range(1, 10):
        if not check(board, x, y, val):
            continue
        board[x][y] = val
        i, j = findNextFreeBlock(board, x, y)
        if bruteForceSolverHelper(board, i, j):
            return True
        board[x][y] = 0
    return False
