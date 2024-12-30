# Reshape a 1D array of 25 elements into a 5x5 matrix. Then, flatten it back into a 1D array. in python

import numpy as np
array_1d = np.arange(1, 26)  # This creates an array with values from 1 to 25

# Print the original 1D array
print("Original 1D Array:")
print(array_1d)

# Reshape the 1D array
matrix_5x5 = array_1d.reshape(5, 5)

# Print the reshaped 5x5 matrix
print("\nReshaped 5x5 Matrix:")
print(matrix_5x5)
flattened_array = matrix_5x5.flatten()
print("\nFlattened 1D Array:")
print(flattened_array)

