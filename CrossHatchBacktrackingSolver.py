# Cross Hatch Backtracking Algorithm Code Source: https://www.geeksforgeeks.org/sudoku-backtracking-7/

from initializeBoard import initializeBoard
from printBoard import printBoard


def build_pos_and_rem(board, pos, rem):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] > 0:
                if board[i][j] not in pos:
                    pos[board[i][j]] = []
                pos[board[i][j]].append([i, j])
                if board[i][j] not in rem:
                    rem[board[i][j]] = 9
                rem[board[i][j]] -= 1

    for i in range(1, 10):
        if i not in pos:
            pos[i] = []
        if i not in rem:
            rem[i] = 9


def build_graph(graph, pos, board):
    for k, v in pos.items():
        if k not in graph:
            graph[k] = {}

        row = list(range(0, 9))
        col = list(range(0, 9))

        for cord in v:
            row.remove(cord[0])
            col.remove(cord[1])

        if len(row) == 0 or len(col) == 0:
            continue

        for r in row:
            for c in col:
                if board[r][c] == 0:
                    if r not in graph[k]:
                        graph[k][r] = []
                    graph[k][r].append(c)


def is_safe(board, x, y):
    key = board[x][y]
    for i in range(0, 9):
        if i != y and board[x][i] == key:
            return False
        if i != x and board[i][y] == key:
            return False
    r_start = int(x / 3) * 3
    r_end = r_start + 3
    c_start = int(y / 3) * 3
    c_end = c_start + 3
    for i in range(r_start, r_end):
        for j in range(c_start, c_end):
            if i != x and j != y and board[i][j] == key:
                return False
    return True


def fill_matrix(graph, board, k, keys, r, rows):
    for c in graph[keys[k]][rows[r]]:
        if board[rows[r]][c] > 0:
            continue
        board[rows[r]][c] = keys[k]
        if is_safe(board, rows[r], c):
            if r < len(rows) - 1:
                if fill_matrix(graph, board, k, keys, r + 1, rows):
                    return True
                else:
                    board[rows[r]][c] = 0
                    continue
            else:
                if k < len(keys) - 1:
                    if fill_matrix(graph, board, k + 1, keys, 0, list(graph[keys[k + 1]].keys())):
                        return True
                    else:
                        board[rows[r]][c] = 0
                        continue
                return True
        board[rows[r]][c] = 0
    return False


def crossHatchBacktrackingSolver(grid):
    board = initializeBoard(grid)
    pos = {}
    rem = {}
    graph = {}
    build_pos_and_rem(board, pos, rem)
    rem = {k: v for k, v in sorted(rem.items(), key=lambda item: item[1])}
    build_graph(graph, pos, board)
    key_s = list(rem.keys())
    fill_matrix(graph, board, 0, key_s, 0, list(graph[key_s[0]].keys()))
    # printBoard(board)
