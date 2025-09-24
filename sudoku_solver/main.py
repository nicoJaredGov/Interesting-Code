from solvers.sudoku_solver import basic_solver, get_puzzle_matrix
from solvers.utils import *

if __name__ == "__main__":
    # string representation of sudoku puzzle - serialized left to right, top-down
    # 0 represents the empty cells needed to be filled in
    puzzle1 = "800607030720031080901040200009200106003000400507006300005060809040890017090102005"
    puzzle2 = "084650000300490050010007400063502190075060230092703540009100060040039005000046910"
    puzzle3 = "006100000007500300004008607000000000003040200050800700030001020090200800000000061"

    a = get_2d_array(puzzle1)
    draw(a)
    r, c, b = get_sudoku_sets(a)
    print_sets(r, c, b)
