from utils import *


class SudokuSolverV2:
    def __init__(self, puzzle_str: None | str):
        if puzzle_str is not None:
            self.load_new(puzzle_str)

    def load_new(self, puzzle_str: str):
        self.puzzle_str = puzzle_str
        self.puzzle_mat = get_2d_array(puzzle_str)
        self.sets = get_sudoku_sets(self.puzzle_mat)

    def draw(self):
        draw(self.puzzle_mat)

    def print_info(self):
        print_sets(self.sets)

    def solve(self):
        pass
