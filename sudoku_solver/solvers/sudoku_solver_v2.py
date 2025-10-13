from .utils import *


class SudokuSolverV2:
    universal = set(range(1, 9))

    def __init__(self, puzzle_str: None | str):
        if puzzle_str is not None:
            self.load_new(puzzle_str)

    def load_new(self, puzzle_str: str):
        self.puzzle_str = puzzle_str
        self.puzzle_mat = get_2d_array(puzzle_str)
        self.empty_cells = get_empty_cells(self.puzzle_mat)
        self.rows, self.cols, self.blocks = get_sudoku_sets(self.puzzle_mat)

        self.filled = set()

    def draw(self, with_color=True):
        if with_color:
            draw_color(self.puzzle_mat, self.filled)
        else:
            draw(self.puzzle_mat)

    def print_info(self):
        print_sets(self.rows, self.cols, self.blocks)

    def solve(self):
        self.filled = set()

        while len(self.empty_cells) != 0:
            num_filled = len(self.filled)

            for row, col in self.empty_cells:
                block_index = 3 * (row // 3) + (col // 3)
                existing = self.rows[row].union(self.cols[col], self.blocks[block_index])
                available = SudokuSolverV2.universal - existing

                if len(available) == 1:
                    # update grid
                    (new_val,) = available
                    self.puzzle_mat[row][col] = new_val

                    # update sets
                    self.rows[row].add(new_val)
                    self.cols[col].add(new_val)
                    self.blocks[block_index].add(new_val)

                    self.filled.add((row, col))

            # after iterating through all the empty cells in this iteration, update empty cells
            self.empty_cells -= self.filled

        if len(self.filled) == num_filled:
            print("Solution not found.")
            return

        print("Solved!")
        return
