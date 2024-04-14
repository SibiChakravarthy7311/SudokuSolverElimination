from nextFreeBlock import findNextFreeBlock
from bruteForceSolver import bruteForceSolverHelper
from BitMaskSolver import bitMaskSolver
from DancingLinks import dlxSolver
from CrossHatchBacktrackingSolver import crossHatchBacktrackingSolver
from initializeGraph import initializeGraph
from initializeBoard import initializeBoard
from EliminationSolver import eliminationSolverHelper, initialSolver, findPossibles
from matplotlib import pyplot
import timeit
from functools import partial
import numpy as np
from time import time
import pandas as pd
import subprocess
import os
import zipfile


# graph plotting helper function for grids from the dataset
def plot_time(func, inputs, repeats, n_tests):
    x, y, y_err = [], [], []
    totalTime = 0
    for index, row in inputs.iterrows():
        print(index)
        grid = row['puzzle']
        # difficulty = row['difficulty']
        timer = timeit.Timer(partial(func, grid))
        t = timer.repeat(repeat=repeats, number=n_tests)
        x.append(index+1)
        totalTime += np.mean(t)
        y.append(totalTime)
        y_err.append(np.std(t) / np.sqrt(len(t)))
    pyplot.errorbar(x, y, yerr=y_err, fmt='-o', label=func.__name__)


# graph plotting helper function for individual grids
def plot_time_individual(func, inputs, repeats, n_tests):
    x, y, y_err = [], [], []
    totalTime = 0
    ct = 0
    for grid in inputs:
        ct += 1
        # difficulty = row['difficulty']
        timer = timeit.Timer(partial(func, grid))
        t = timer.repeat(repeat=repeats, number=n_tests)
        x.append(ct)
        totalTime += np.mean(t)
        y.append(totalTime)
        y_err.append(np.std(t) / np.sqrt(len(t)))
    pyplot.errorbar(x, y, yerr=y_err, fmt='-o', label=func.__name__)


# to run functions and plot graph for data from the dataset
def plot_times(functions, inputs, repeats=3, n_tests=1, file_name_prefix=""):
    for func in functions:
        plot_time(func, inputs, repeats, n_tests)
    pyplot.legend()
    pyplot.xlabel("Puzzle Count")
    pyplot.ylabel("Total Time")
    if not file_name_prefix:
        pyplot.show()
    else:
        pyplot.savefig(file_name_prefix + str(round(time() * 1000)))


# to run functions and plot graph
def plot_times_individual(functions, inputs, repeats=3, n_tests=1, file_name_prefix=""):
    for func in functions:
        plot_time_individual(func, inputs, repeats, n_tests)
    pyplot.legend()
    pyplot.xlabel("Puzzle Count")
    pyplot.ylabel("Total Time")
    if not file_name_prefix:
        pyplot.show()
    else:
        pyplot.savefig(file_name_prefix + str(round(time() * 1000)))


def eliminationSolver(grid):
    board = initializeBoard(grid)
    possibles = findPossibles(board)
    initialSolver(board, possibles, graph)
    i, j = findNextFreeBlock(board, 0, 0)
    eliminationSolverHelper(board, possibles, graph, i, j)


def bruteForceSolver(grid):
    board = initializeBoard(grid)
    i, j = findNextFreeBlock(board, 0, 0)
    bruteForceSolverHelper(board, i, j)


graph = initializeGraph()
# Question grids
grids = ["1..5.37..6.3..8.9......98...1.......8761..........6...........7.8.9.76.47...6.312"] * 10
# hardData = ["..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97.."] * 10

# file_name = "sudoku_data.csv"
file_name = "sudoku_data_100_rows.csv"
# file_name = "sudoku_data_1000_rows.csv"
# file_name = "sudoku_data_1000_rows.csv"

if not os.path.exists(file_name):
    dataset_name = "radcliffe/3-million-sudoku-puzzles-with-ratings"
    subprocess.run(["kaggle", "datasets", "download", "-d", dataset_name])
    zip_file_name = "3-million-sudoku-puzzles-with-ratings.zip"
    extracted_csv_name = "sudoku-3m.csv"
    if os.path.exists(zip_file_name):
        with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
            zip_ref.extractall()
        if os.path.exists(extracted_csv_name):
            os.rename(extracted_csv_name, file_name)
data = pd.read_csv(file_name)

# plot_times([eliminationSolver, bitMaskSolver, crossHatchBacktrackingSolver, bruteForceSolver, dlxSolver],
#                data, repeats=1, n_tests=1, file_name_prefix="plot-")
# plot_times([eliminationSolver, bitMaskSolver, crossHatchBacktrackingSolver, bruteForceSolver],
#                data, repeats=1, n_tests=1, file_name_prefix="plot-")
# plot_times([eliminationSolver, crossHatchBacktrackingSolver],
#                data, repeats=1, n_tests=1, file_name_prefix="plot-")
# plot_times([eliminationSolver, dlxSolver],
#                data, repeats=1, n_tests=1, file_name_prefix="plot-")
# plot_times_individual([eliminationSolver, bitMaskSolver, crossHatchBacktrackingSolver, bruteForceSolver, dlxSolver],
#                grids, repeats=1, n_tests=1, file_name_prefix="plot-")
# plot_times_individual([eliminationSolver, bitMaskSolver, crossHatchBacktrackingSolver, bruteForceSolver, dlxSolver],
#                hardData, repeats=1, n_tests=1, file_name_prefix="plot-")
plot_times_individual([eliminationSolver, bitMaskSolver, crossHatchBacktrackingSolver, bruteForceSolver, dlxSolver],
               grids, repeats=1, n_tests=1, file_name_prefix="plot-")
# plot_times_individual([eliminationSolver, dlxSolver],
#                hardData, repeats=1, n_tests=1, file_name_prefix="plot-")
