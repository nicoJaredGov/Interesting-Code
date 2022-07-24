from asyncore import close_all
import numpy as np

#NOTE current assumption is 9*9 typical sudoku puzzle

# string representation of sudoku puzzle - serialized left to right, top-down
# 0 represents the empty cells needed to be filled in
puzzle1 = "800607030720031080901040200009200106003000400507006300005060809040890017090102005"

#converts string representation to a numpy matrix representation
def get_puzzle_matrix(puzzle_str):
    puzzle_array = list(puzzle_str)
    puzzle_array= [int(i) for i in puzzle_array]
    puzzle_matrix = np.array(puzzle_array)
    puzzle_matrix = np.reshape(puzzle_matrix,(9,9))
    print(puzzle_matrix)
    return puzzle_matrix

#converts matrix representation to sets representation
def get_puzzle_sets(puzzle_mat):
    #list of sets for each row, column and block
    row_sets = []
    col_sets = []
    block_sets = []

    #use two indices to iterate through rows and columns interchangeably for both row sets and column sets
    for idx1 in range(9):
        #create new temporary sets for each index
        temp_rset = set()
        temp_cset = set()

        #update sets
        for idx2 in range(9):
            #update row set
            curr_rvalue = puzzle_mat[idx1][idx2]
            if curr_rvalue != 0:
                temp_rset.add(curr_rvalue)
            #update column set
            curr_cvalue = puzzle_mat[idx2][idx1]
            if curr_cvalue != 0:
                temp_cset.add(curr_cvalue)

        #add temp set to the lists
        row_sets.append(temp_rset)
        col_sets.append(temp_cset)
    
    #obtain block sets 0->0,0  1->0,3  2->0,6
    for idx3 in range(0,7,3):
        for idx4 in range(0,7,3):
            #create new temporary block set
            temp_bset = set()

            #update set for each value in block
            for i in range(0,3):
                for j in range(0,3):
                    curr_bvalue = puzzle_mat[idx3+i][idx4+j]
                    if curr_bvalue != 0:
                        temp_bset.add(curr_bvalue)
            
            #add temp set to the list
            block_sets.append(temp_bset)
            
    
    print("Row sets: ")
    print(row_sets)
    print("\nCol sets: ")
    print(col_sets)
    print("\nBlock sets: ")
    print(block_sets)

    return row_sets,col_sets,block_sets

#a basic sudoku solver
'''def basic_solver(puzzle_mat,num_emp_cells):
    for i in range(9):
        value_set = set()
        for j in range(9):
            if puzzle_mat[i][j] == 0:'''

def basic_solver_run(puzzle):
    #get matrix form of string puzzle
    puzzle_mat = get_puzzle_matrix(puzzle)
    get_puzzle_sets(puzzle_mat)

    #determine how many cells are empty
    num_empty_cells = 81 - np.count_nonzero(puzzle_mat)
    print(num_empty_cells)

basic_solver_run(puzzle1)