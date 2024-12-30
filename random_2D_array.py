# Compute the mean, median, standard deviation, and variance of a random 2D array.

import numpy as np

# Create a random 2D array of size (4, 5)
array_2d = np.random.rand(4, 5)

# Compute the mean
mean_value = np.mean(array_2d)

# Compute the median
median_value = np.median(array_2d)

# Compute the standard deviation
std_deviation = np.std(array_2d)

# Compute the variance
variance_value = np.var(array_2d)

# Print the results
print("2D Array:\n", array_2d)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)
print("Variance:", variance_value)
