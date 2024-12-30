# Create two random arrays of the same shape (3x4). Perform element-wise addition, multiplication, and division.

import numpy as np

# Create two random arrays of shape (3, 4)
arr1 = np.random.rand(3, 4)
arr2 = np.random.rand(3, 4)

# Perform element-wise addition
addition_result = arr1 + arr2

# Perform element-wise multiplication
multiplication_result = arr1 * arr2
division_result = np.divide(arr1, arr2, out=np.zeros_like(arr1), where=arr2!=0)

# Print the results
print("Array 1:\n", arr1)
print("Array 2:\n", arr2)
print("Addition Result:\n", addition_result)
print("Multiplication Result:\n", multiplication_result)
print("Division Result:\n", division_result)