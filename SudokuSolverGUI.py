# Reference Project: https://github.com/techwithtim/Sudoku-GUI-Solver/blob/master/GUI.py

import pygame
import time
from initializeBoard import initializeBoard
from nextFreeBlock import findNextFreeBlock
from check import check
from EliminationSolver import eliminationSolverGUI

pygame.font.init()


class Grid:
    grid = "78.4..12.6...75..9...6.1.78..7.4.26...1.5.93.9.4.6...5.7.3...1212...74...492.6..7"
    # grid = "1..5.37..6.3..8.9......98...1.......8761..........6...........7.8.9.76.47...6.312"
    # grid = "..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97.."
    board = initializeBoard(grid)

    def __init__(self, rows, cols, width, height, win):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.update_model()
        self.selected = None
        self.win = win

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if valid(self.model, val, (row, col)) and self.solve():
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def draw(self):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.win, (0, 0, 0), (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(self.win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(self.win)

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def click(self, pos):
        """
        :param: pos
        :return: (row, col)
        """
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y), int(x))
        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True

    def solve(self, x=0, y=0):
        find = findNextFreeBlock(self.model, x, y)
        if find[0] is None:
            return True
        else:
            row, col = find
        for i in range(1, 10):
            if not check(self.model, row, col, i):
                continue
            self.model[row][col] = i
            if self.solve(row, col):
                return True
            self.model[row][col] = 0
        return False

    def solve_gui(self, delayTime, x=0, y=0):
        self.update_model()
        find = findNextFreeBlock(self.model, x, y)
        if find[0] is None:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if not check(self.model, row, col, i):
                continue
            self.model[row][col] = i
            self.cubes[row][col].set(i)
            self.cubes[row][col].draw_change(self.win, True)
            self.update_model()
            pygame.display.update()
            pygame.time.delay(delayTime)

            if self.solve_gui(delayTime, row, col):
                return True

            self.model[row][col] = 0
            self.cubes[row][col].set(0)
            self.update_model()
            self.cubes[row][col].draw_change(self.win, False)
            pygame.display.update()
            pygame.time.delay(delayTime)

        return False


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            win.blit(text, (x + 5, y + 5))
        elif not (self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def draw_change(self, win, g=True):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        pygame.draw.rect(win, (255, 255, 255), (x, y, gap, gap), 0)

        text = fnt.render(str(self.value), 1, (0, 0, 0))
        win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))
        if g:
            pygame.draw.rect(win, (0, 255, 0), (x, y, gap, gap), 3)
        else:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def redraw_window(win, board, time, strikes):
    win.fill((255, 255, 255))
    # Draw time
    fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render("Time: " + format_time(time), 1, (0, 0, 0))
    win.blit(text, (540 - 160, 560))
    # Draw Strikes
    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    win.blit(text, (20, 560))
    # Draw grid and board
    board.draw()


def format_time(secs):
    sec = secs % 60
    minute = secs // 60
    hour = minute // 60

    mat = " " + str(minute) + ":" + str(sec)
    return mat


def main():
    delayTime = 300

    # win = pygame.display.set_mode((590, 610))
    # pygame.display.set_caption("Sudoku")
    # board = Grid(9, 9, 540, 540, win)
    # start = time.time()
    # strikes = 0
    #
    # play_time = round(time.time() - start)
    # redraw_window(win, board, play_time, strikes)
    # pygame.display.update()
    # time.sleep(2)
    # board.solve_gui(delayTime)
    # play_time = round(time.time() - start)
    # redraw_window(win, board, play_time, strikes)
    # pygame.display.update()
    # time.sleep(2)

    win = pygame.display.set_mode((590, 610))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540, win)
    start = time.time()
    strikes = 0

    play_time = round(time.time() - start)
    redraw_window(win, board, play_time, strikes)
    pygame.display.update()
    time.sleep(2)
    eliminationSolverGUI(board, delayTime)
    play_time = round(time.time() - start)
    redraw_window(win, board, play_time, strikes)
    pygame.display.update()


main()
time.sleep(2)
# val = input("Waiting to Exit: ")
pygame.quit()
