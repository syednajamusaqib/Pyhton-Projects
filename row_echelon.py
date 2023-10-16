import numpy as np 

"""
There are basically four steps in this approach
Step 1: Check for Non Zero Row
Step 2: Swap Rows
Step 3: Make Pivot element of Pivot Row "1"
Step 4: Eliminate elements below pivots to get Row-Echelon Form  

"""

# Function to check whether matrix is zero matrix or not
def is_zero_matrix(matrix):
    rows = len(matrix)
    if rows == 0:
        return False
    cols = len(matrix[0])
    if cols == 0:
        return False
    for row in range(rows):
        for col in range(cols):
            if matrix[row,col] !=0:
                return False
    return True

# Function to check for empty matrix
def is_empty(matrix):
    rows = len(matrix)
    if rows == 0:
        return True
    cols = len(matrix[0])
    if cols == 0:
        return True

# Function to Find non zero row of the matrix
def find_nonzero_row(matrix, pivot_row, col):
    nrows = len(matrix)
    for row in range(pivot_row, nrows):
        if matrix[row, col] != 0:
            return row
    return None

# Function to swap non zero row with the pivot row
def swap_rows(matrix, row1, row2):
    matrix[[row1, row2]] = matrix[[row2, row1]]  

# This function will make pivot element to be 1
def make_pivot_one(matrix, pivot_row, col):
    pivot_element = matrix[pivot_row, col]
    matrix[pivot_row] //= pivot_element

# Function to eliminate all the entries below pivot element to be 0
def eliminate_below(matrix, pivot_row, col):
    nrows = len(matrix)
    pivot_element = matrix[pivot_row, col]
    for row in range(pivot_row + 1, nrows):
        factor = matrix[row, col]
        matrix[row] -= factor * matrix[pivot_row]

# Converting matrix into row echelon form by implementing above functions
def row_echelon_form(matrix):
    rows = len(matrix)
    ncols = len(matrix[0])
    pivot_row = 0

    for col in range(ncols):
        nonzero_row = find_nonzero_row(matrix, pivot_row, col)
        if nonzero_row is not None:
            swap_rows(matrix, pivot_row, nonzero_row)
            make_pivot_one(matrix, pivot_row, col)
            eliminate_below(matrix, pivot_row, col)
            pivot_row += 1
    return matrix


# This function will check if a matrix is in row echelon form or not
def is_echelon_form(matrix):
    if not matrix.any():
        return False  # Empty matrix is not in echelon form
    if is_zero_matrix(matrix):
        return True
    
    if len(matrix) == 1:  # matrix with 1 length is already in row echelon form
        return True
    rows = len(matrix)
    cols = len(matrix[0])
    prev_leading_col = -1  # Initialize to an invalid value

    for i in range(rows):
        leading_col_found = False

        for j in range(cols):
            if matrix[i][j] != 0:
                if j <= prev_leading_col:
                    return False  # Leading non-zero element is not to the right
                prev_leading_col = j
                leading_col_found = True
                break

        if not leading_col_found and any(matrix[i][j] != 0 for j in range(cols)):
            return False  # All elements after the leading zeros should be zero

    return True

# Taking input from the user

rows = abs(int(input("Enter number of rows: "))) # Taking number of rows as input
cols = abs(int(input("Enter number of columns: "))) # Taking number of columns as input
matrix = [] # Initializing empty list so that later on we can append lists into it to make it matrix
for i in range(rows):
    row = []
    for col in range(cols):
        number = float(input())
        row.append(number) # Appending number to the row
    matrix.append(row) # Appending to list
matrix_np = np.array(matrix) # Converting into numpy array


if is_zero_matrix(matrix_np): # Checking if matrix is zero matrix
    print("Zero matrix is already in row echelon form")
elif is_empty(matrix_np):
    print("Empty Matrix is not in Row echelon form")
else:
    print(f"Before Converting into REF \n {matrix_np}")
    result = row_echelon_form(matrix_np)
    print(f"After Converting into REF \n {result}")
    if is_echelon_form(result):
        print("In REF")
    else:
        print("Not in REF")





