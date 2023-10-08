import numpy as np

"""
There are basically four steps in this approach
Step 1: Check for Non Zero Row
Step 2: Swap Rows
Step 3: Make Pivot element of Pivot Row "1"
Step 4: Eliminate elements below pivots to get Row-Echelon Form  
"""

# Function to check if matrix is in REF

def is_row_echelon_form(matrix):
    if not matrix.any():
        return False
    
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    prev_leading_col = -1

    for row in range(rows):
        leading_col_found = False
        for col in range(cols):
            if matrix[row,col] != 0:
                if col <= prev_leading_col:
                    return False
                prev_leading_col = col
                leading_col_found = True
                break
        if not leading_col_found and any(matrix[row,col] != 0 for col in range(cols)):
            return False
    return True
    
# Completing Step 1
"""
This function will check first entries of all the rows. If in any of rows first entry is not zero, 
It means we have the non zero row which can be used as our first row. 
"""

def find_nonzero_row(matrix, pivot_row, col):
    nrows = matrix.shape[0]
    for row in range(pivot_row, nrows):
        if matrix[row, col] != 0:
            return row
    return None

# Completing Step 2
# Swapping rows so that we can have our non zero row on the top of the matrix
def swap_rows(matrix, row1, row2):
    matrix[[row1, row2]] = matrix[[row2, row1]]  

# Completing Step 3
"""
We will make our pivot element 1 by simply dividing(Floor division) our pivot_row
(Row where we are currently performing operations) by pivot_element
"""
def make_pivot_one(matrix, pivot_row, col):
    pivot_element = matrix[pivot_row, col]
    matrix[pivot_row] //= pivot_element
    # print(pivot_element)

# Completing Step 4
"""
When our pivot_element is set to 1, the next step is to make all the elements below 
pivot_element 0.
"""
def eliminate_below(matrix, pivot_row, col):
    nrows = matrix.shape[0]
    pivot_element = matrix[pivot_row, col]
    for row in range(pivot_row + 1, nrows):
        factor = matrix[row, col]
        # print(factor)
        matrix[row] -= factor * matrix[pivot_row]
        # print(matrix[row])

# Implementing above functions

def row_echelon_form(matrix):
    nrows = matrix.shape[0]
    ncols = matrix.shape[1]
    pivot_row = 0
# this will run for number of column times. If matrix has 3 columns this loop will run for 3 times
    for col in range(ncols):
        nonzero_row = find_nonzero_row(matrix, pivot_row, col)
        if nonzero_row is not None:
            swap_rows(matrix, pivot_row, nonzero_row)
            make_pivot_one(matrix, pivot_row, col)
            eliminate_below(matrix, pivot_row, col)
            pivot_row += 1
    print(matrix)
    return matrix

# Generating Random matrices for as Test cases
# It is optional to use this function
def generate_random_matrix(rows, cols, min_value, max_value):
    return np.random.randint(min_value, max_value + 1, size=(rows, cols), dtype=int)


matrix = np.array([[5,4,0,2],[10,2,5,9],[0,0,0,0]])
# for i in range(100):
    # matrix = generate_random_matrix(3,4,0,99)
result = row_echelon_form(matrix)
if is_row_echelon_form:
        print("In REF")
else:
        print("Not in REF--------------->")

# print(result)
