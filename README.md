# Sudoku Solver using Graph Coloring and Backtracking

This project is aimed at developing efficient methods for solving Sudoku puzzles. The main objective is to implement various solving strategies and compare their performance using real-world Sudoku datasets.

## Project Structure

The main driver file in this project is the `sudokuSolver.py` file which runs the solver algorithms and plots their performances. There are 5 methods used in this project to solve the sudoku puzzle:

- `EliminationSolver.py`: Elimination Method, the solver developed in this project
- `bruteForceSolver.py`: Brute Force Method
- `BitMaskSolver.py`: Brute Force Bitmask Method
- `CrossHatchBacktrackingSolver.py`: Cross Hatch Backtracking Method
- `DancingLinks.py`: Dancing Links Method

Other files include:

- `check.py`: Utility function for Brute Force Method to check the validity of a value in a cell.
- `dlx.py`: Module for Dancing Links solver method.
- `fillAndEliminate.py`: Utility function for the Elimination Method.
- `initializeBoard.py`: Module to initialize the Sudoku board.
- `initializeGraph.py`: Module to initialize the graph structure for Sudoku solving.
- `nextFreeBlock.py`: Module to find the next free block in the Sudoku grid.
- `printBoard.py`: Module to print the Sudoku board in output.
- `sudokuSolver.py`: Main driver file that runs the solver algorithms on sudoku datasets and plots their performances.
- `sudokuSolverGUI.py`: Driver file that runs and visualizes the sudoku solving using the Elimination Method and Brute Force Method.

## Installation Instructions

Follow these steps to set up the Sudoku Solver project on your local machine:

1. **Clone the Repository**: Open your terminal or command prompt and run the following command to clone the repository:

```bash
git clone https://github.com/SibiChakravarthy7311/SudokuSolverElimination
```

2. **Navigate to Project Directory**: Use the `cd` command to navigate to the project directory:
```bash
cd SudokuSolverElimination
```

3. **Install Project Dependencies**: Run the following command to install the required dependencies:
```bash
pip install -r requirements.txt
```


This command will install all the dependencies listed in the `requirements.txt` file.

## Usage

After installation, run the `sudokuSolver.py` file using the command:

```bash
python sudokuSolver.py
```


This will generate a graph plot in the project directory, which displays the solver performance.

In the sudokuSolver.py file, lines 116 to 131 contain different versions of the plot_times functions, most of which are commented out. You can refer to them and experiment by adding or removing functions to compare results. Additionally, you can change the data source using the filename or individual grids.

Please note that the file "sudoku_data.csv" is not included in this project due to its large size. However, it can be downloaded from the Kaggle website [here](https://www.kaggle.com/datasets/radcliffe/3-million-sudoku-puzzles-with-ratings). If you run the sudokuSolver.py with the file_name set to "sudoku_data.csv", it will download the file from the Kaggle website the first time you run the program. This may take some time, so ensure you have an active internet connection.

You can also experiment with the sudokuSolverGUI.py file by running the command:
```bash
python sudokuSolverGUI.py
```


This will provide a visual demonstration of how the Sudoku is being solved. You can adjust the delayTime parameter to vary the speed of solving. Additionally, you can try different solving methods (board.solve_gui for brute force method and eliminationSolverGUI for the elimination method) and different grids (as shown in lines 14-16).

# Dataset

The Sudoku puzzles used in this project are sourced from the Kaggle dataset [Sudoku puzzles](https://www.kaggle.com/datasets/radcliffe/3-million-sudoku-puzzles-with-ratings) by radcliffe. The dataset contains puzzles of varying difficulty levels, which are used for testing and evaluating the solver algorithms.

# License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).