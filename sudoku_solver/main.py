from solvers.sudoku_solver_v2 import SudokuSolverV2

if __name__ == "__main__":
    # string representation of sudoku puzzle - serialized left to right, top-down
    # 0 represents the empty cells needed to be filled in
    puzzle2 = "050703060007000800000816000000030000005000100730040086906000204840572093000409000"

    # r, c, b = get_sudoku_sets(a)
    # print_sets(r, c, b)
    # d = get_empty_cells(a)
    # print(d)

    solver = SudokuSolverV2(puzzle_str=puzzle2)
    solver.draw()
    solver.print_info()
    solver.solve()
    solver.draw()
