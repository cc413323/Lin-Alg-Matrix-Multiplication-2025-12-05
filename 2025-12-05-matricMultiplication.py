from tabulate import tabulate
import csv


row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1.2, 3]
M = [ row_1, row_2, row_3]

row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1.2, 3]
row_4 = [0, 1, -1, 6]
N = [ row_1, row_2, row_3, row_4]

print(tabulate(M))
print("\n")
print(tabulate(N))
print("\n")

# Challenge 1
def matrix_dimensions(A):
  num_rows = len(A)
  num_cols = len(A[0])
  return((num_rows,num_cols))
print("the dimensions of the matrix: " + str(matrix_dimensions(M)))

# Challenge 2
def can_multiply_matrices(A,B):
  if (len(A[0])==len(B)):
    return True
  else:
    return False
print("Can MN multiply? " + str(can_multiply_matrices(M, N)))
print("Can NM multiply? " + str(can_multiply_matrices(N, M)))

# Challenge 3
def matrix_product_entry(A,B,i,j):
    if not can_multiply_matrices(A,B):
        return
    else:
        ret = 0
        for k in range(len(A[0])):
            ret += A[i][k]*B[k][j]
        return ret
print("product of MN at (0,2): " + str(matrix_product_entry(M,N,0,2)))

# Challenge 4
# Write a function that multiplies two matrices A and B

# Returns the matrix product

def matrix_product(A,B):

  # Should probably check first to see if the matrices can be multiplied!

  # Initialize a new empty list for your row lists 
  P = []
  # Use matrix_product_entry!

  return P

# Challenge 5
# Write a function that transposes a matrix
  
def matrix_transpose(A):
  
  M = []
  return M
