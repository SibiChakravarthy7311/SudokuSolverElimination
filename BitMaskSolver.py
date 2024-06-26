# Bitmask Algorithm Code Source: https://www.geeksforgeeks.org/sudoku-backtracking-7/

from initializeBoard import initializeBoard
from printBoard import printBoard


def isSafe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def bitMaskSolverHelper(grid, row, col):
    if row == 9 - 1 and col == 9:
        return True

    if col == 9:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return bitMaskSolverHelper(grid, row, col + 1)
    for num in range(1, 9 + 1, 1):
        if isSafe(grid, row, col, num):
            grid[row][col] = num
            if bitMaskSolverHelper(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


def bitMaskSolver(grid):
    board = initializeBoard(grid)
    bitMaskSolverHelper(board, 0, 0)
    # printBoard(board)

