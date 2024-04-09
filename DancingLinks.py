# Dancing Links Algorithm Code Source: https://github.com/eric-ycw/sudoku-dlx


import dlx
from printBoard import printBoard


class Sudoku(object):
    def solve(self, grid_str):
        solver = dlx.DLX()
        solver.create_matrix(grid_str)
        dlx_solution, found = solver.search([])
        return dlx_solution, found

    def output_solution(self, dlx_solution, found):
        """Converts a solution set from Dancing Links into a grid"""
        if not found:
            print('Solution not found')
            return
        solution = [0] * 81
        result = []
        current = []
        for i in dlx_solution:
            val = i.row % 9
            if val == 0:
                val = 9
            solution[(i.row - 1) // 9] = val
            current.append(val)
            if len(current) == 9:
                result.append(current.copy())
                current = []
        return result


def dlxSolver(grid):
    s = Sudoku()
    solution, found = s.solve(grid)
    board = s.output_solution(solution, found)
    # printBoard(board)
