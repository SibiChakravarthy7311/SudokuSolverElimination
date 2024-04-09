def findNextFreeBlock(board, x, y):
    for j in range(y, 9):
        if not board[x][j]:
            return x, j
    for i in range(x+1, 9):
        for j in range(9):
            if not board[i][j]:
                return i, j
    return None, None
