# Reverse the rows and columns of a 5x5 matrix of integers.

import numpy as np

matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

# Reverse the rows and columns
reversed_matrix = np.flipud(np.fliplr(matrix))


print(reversed_matrix)
