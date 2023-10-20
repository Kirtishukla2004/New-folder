import numpy as np
import pandas as pd

matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# Create a 2D array from the matrix
array_2d = np.array(matrix)

print(array_2d)


# Define a matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],[7,8,9]])

# Calculate the transpose of the matrix
transpose_matrix = matrix.T
add=array_2d+transpose_matrix
print(add)
x=np.arange(1,11)
s1=pd.Series(x,x*2)
s2=pd.Series(x**2,x)
print(s1)
print(s2)