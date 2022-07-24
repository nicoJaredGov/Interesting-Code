from hashlib import new
import numpy as np

#NOTE current assumption is 9*9 typical sudoku puzzle

#converts string representation to a numpy matrix representation
def get_puzzle_matrix(puzzle_str):
    puzzle_array = list(puzzle_str)
    puzzle_array= [int(i) for i in puzzle_array]
    puzzle_matrix = np.array(puzzle_array)
    puzzle_matrix = np.reshape(puzzle_matrix,(9,9))
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
            
    return row_sets,col_sets,block_sets

#print sets in console
def print_sets(row_sets, col_sets, block_sets):
    print("---------------------------------")
    print("row sets: ")
    print(row_sets)
    print("\ncol sets: ")
    print(col_sets)
    print("\nblock sets: ")
    print(block_sets)
    print("---------------------------------")

#draw solution from string
def draw(puzzle):
    for r in range(len(puzzle)):
        if r == 0 or r == 3 or r == 6:
            print("+-------+-------+-------+")
        for c in range(len(puzzle[r])):
            if c == 0 or c == 3 or c ==6:
                print("| ", end = "")
            if puzzle[r][c] != 0:
                print(puzzle[r][c], end = " ")
            else:
                print(end = "  ")
            if c == 8:
                print("|")
    print("+-------+-------+-------+")

#get empty cell locations
def get_empty_cells(puzzle_mat):
    empty_cells = []
    for i in range(9):
        for j in range(9):
            if puzzle_mat[i][j] == 0:
                empty_cells.append((i,j))
    return empty_cells

'''a basic sudoku solver'''
def basic_solver(puzzle):
    #get matrix form of string puzzle
    puzzle_mat = get_puzzle_matrix(puzzle)
    draw(puzzle_mat)

    #get sets form from matrix form
    rsets,csets,bsets = get_puzzle_sets(puzzle_mat)
    universal_set = set([1,2,3,4,5,6,7,8,9])
    print(universal_set)
    print_sets(rsets, csets, bsets)

    #get locations of empty cells
    empty_cells = get_empty_cells(puzzle_mat)
    num_empty_cells = len(empty_cells)
    print("empty cells: ", empty_cells)

    while num_empty_cells != 0:
        print("\niter ", num_empty_cells)
        curr_num_empty = num_empty_cells

        for empty_cell_idx in range(len(empty_cells)):
            #check the union of row, col and block
            x = empty_cells[empty_cell_idx][0]
            y = empty_cells[empty_cell_idx][1]
            bset_idx = 3*(x//3) + y//3
            value_set = rsets[x].union(csets[y], bsets[bset_idx])

            #get compliment= of above set
            comp_set = universal_set - value_set

            '''print("empty_cell: ", empty_cells[empty_cell_idx])
            print("sets: ", rsets[x],csets[y],bsets[bset_idx])
            print("value set: ", value_set)
            print("comp set: ", comp_set)'''

            #check if there is only one value that can fit there
            if len(comp_set) == 1:
                #get this value and update matrix
                (new_val,) = comp_set
                puzzle_mat[x][y] = new_val

                #add this value to the respective sets as well
                rsets[x].add(new_val)
                csets[y].add(new_val)
                bsets[bset_idx].add(new_val)

                #remove as empty cell
                empty_cells.pop(empty_cell_idx)
                
                '''print(puzzle_mat)
                print_sets(rsets, csets, bsets)
                print(empty_cells)'''

                num_empty_cells-=1

                #break out of loop because we have to iterate again after empty cell removed
                break
        
        #print(puzzle_mat)

        if num_empty_cells == curr_num_empty:
            print("no solution")
            return

    return puzzle_mat

            
'''MAIN HERE'''
# string representation of sudoku puzzle - serialized left to right, top-down
# 0 represents the empty cells needed to be filled in
puzzle1 = "800607030720031080901040200009200106003000400507006300005060809040890017090102005"
puzzle2 = "084650000300490050010007400063502190075060230092703540009100060040039005000046910"

'''solution1 = basic_solver(puzzle1)
print(solution1)'''

'''solution2 = basic_solver(puzzle2)
print(solution2)'''

puzzle3 = "006100000007500300004008607000000000003040200050800700030001020090200800000000061"
sol3 = basic_solver(puzzle3)
draw(sol3)