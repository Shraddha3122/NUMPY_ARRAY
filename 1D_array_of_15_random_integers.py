# Create a 1D array of 15 random integers between 1 and 100. Replace all elements less than 50 with -1.

import numpy as np

# Create a 1D array of 15 random integers between 1 and 100
random_array = np.random.randint(1, 101, size=15)

print("Original Array:")
print(random_array)

# Replace all elements less than 50 with -1
random_array[random_array < 50] = -1
print("\nModified Array (elements < 50 replaced with -1):")
print(random_array)

