import numpy as np


def get_2d_array(puzzle_str: str):
    """
    converts string representation of a sudoku board to a 2d array
    """

    return np.reshape([int(i) for i in puzzle_str], (9, 9))


def get_sudoku_sets(puzzle_mat: np.array):
    """
    returns sets for each row, column, and block for a 9x9 sudoku
    """

    rows = [set(i) - {0} for i in puzzle_mat]
    cols = [set(puzzle_mat[:, j]) - {0} for j in range(9)]
    blocks = [
        set(puzzle_mat[j : j + 3, i : i + 3].flatten()) - {0}
        for j in range(0, 9, 3)
        for i in range(0, 9, 3)
    ]

    return rows, cols, blocks


def draw(puzzle_mat):
    board = "+-------+-------+-------+\n"
    for r in range(len(puzzle_mat)):
        if r in {3, 6, 9}:
            board += "+-------+-------+-------+\n"

        for c in range(len(puzzle_mat[r])):
            if c in {0, 3, 6}:
                board += "| "

            if puzzle_mat[r][c] != 0:
                board += str(puzzle_mat[r][c]) + " "
            else:
                board += "  "

            if c == 8:
                board += "|\n"
    board += "+-------+-------+-------+\n"

    print(board)
    return board


def print_sets(rows, cols, blocks):
    out = "---------------------------------\n"
    out += f"row sets: {rows}\n"
    out += f"col sets: {cols}\n"
    out += f"block sets: {blocks}\n"
    out += "---------------------------------\n"

    print(out)
    return out
