# Create two square matrices of size (3x3) and compute their matrix product.

import numpy as np

# Create two random square matrices of size (3, 3)
matrix1 = np.random.rand(3, 3)
matrix2 = np.random.rand(3, 3)

# Compute the matrix product
matrix_product = np.dot(matrix1, matrix2)

print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Matrix Product:\n", matrix_product)
