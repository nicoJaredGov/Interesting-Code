import numpy as np

# string representation of sudoku puzzle - serialized left to right, top-down
# 0 represents the empty cells needed to be filled in
puzzle1 = "800607030720031080901040200009200106003000400507006300005060809040890017090102005"

def get_puzzle_matrix(puzzle_str):
    puzzle_matrix = list(puzzle_str)
    puzzle_matrix = [int(i) for i in puzzle_matrix]
    puzzle_matrix = np.array(puzzle_matrix)
    puzzle_matrix = np.reshape(puzzle_matrix,(9,9))
    print(puzzle_matrix)
            
def basic_solver(puzzle):
    print(puzzle)

get_puzzle_matrix(puzzle1)