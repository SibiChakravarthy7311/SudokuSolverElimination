def initializeBoard(grid):
    board = [[None] * 9 for i in range(9)]
    ind = 0
    for i in range(9):
        for j in range(9):
            val = 0 if grid[ind] == '.' else int(grid[ind])
            board[i][j] = val
            ind += 1
    return board
