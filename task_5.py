## statistical operations

import numpy as np

## Create a NumPy array of values
marks = np.array([78,85, 90,66,72,88,95,60])

## Perform statistical operations on the array
mean_value = np.mean(marks)
median_value = np.median(marks)
variance_value = np.var(marks)
std_deviation = np.std(marks)
min_value = np.min(marks)
max_value = np.max(marks)
range_value = max_value - min_value

## Print the results
print("Mean value is ", mean_value)
print("Median value is ", median_value)
print("Variance is ", variance_value)
print("Standard deviation is ", std_deviation)
print("Minimum value is ", min_value)
print("Maximum value is ", max_value)
print("Range is ", range_value)