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
    nrows, ncols = matrix.shape
    leading_one_cols = set()
    
    for row in range(nrows):
        leading_one_found = False
        for col in range(ncols):
            if matrix[row, col] != 0:
                if col not in leading_one_cols:
                    leading_one_cols.add(col)
                    leading_one_found = True
                else:
                    return False  # More than one leading 1 in the same column
        if not leading_one_found:
            for r in range(row, nrows):
                if matrix[r, 0] != 0:
                    return False  # Zeros above the leading 1
            
    return True
# Completing Step 1
def find_nonzero_row(matrix, pivot_row, col):
    nrows = matrix.shape[0]
    for row in range(pivot_row, nrows):
        if matrix[row, col] != 0:
            return row
    return None

# Completing Step 2

def swap_rows(matrix, row1, row2):
    matrix[[row1, row2]] = matrix[[row2, row1]]  

# Completing Step 3

def make_pivot_one(matrix, pivot_row, col):
    pivot_element = matrix[pivot_row, col]
    matrix[pivot_row] //= pivot_element
    # print(pivot_element)

# Completing Step 4

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
