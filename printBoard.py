def printBoard(grid):
    line = '---------------------'
    print(line)
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=' ')
            if j == 2 or j == 5:
                print('|', end=' ')
        print()
        if not (i+1) % 3:
            print(line)
    print()
