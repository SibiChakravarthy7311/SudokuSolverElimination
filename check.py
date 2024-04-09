def check(board, x, y, val):
    for j in range(9):
        if board[x][j] == val:
            return False
    for i in range(9):
        if board[i][y] == val:
            return False
    top = (x // 3) * 3
    left = (y // 3) * 3
    for i in range(top, top+3):
        for j in range(left, left+3):
            if board[i][j] == val:
                return False
    return True
