# Calculate the inverse of a square matrix.

import numpy as np

# Create a square matrix (for example, a 3x3 matrix)
matrix = np.array([[4, 7, 2],
                   [3, 6, 1],
                   [2, 5, 3]])

# Print the original matrix
print("Original Matrix:")
print(matrix)

# Calculate the inverse of the matrix
try:
    inverse_matrix = np.linalg.inv(matrix)
    # Print the inverse matrix
    print("\nInverse Matrix:")
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("\nThe matrix is singular and cannot be inverted.")        
