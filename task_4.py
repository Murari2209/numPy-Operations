## Aggregate Operations
import numpy as np

## Create a 2D NumPy array
data = np.array([[10,20,30],[40,50,60],[70,80,90]])

## Perform aggregate operations on the array
row_sum = np.sum(data, axis=1)

col_sum = np.sum(data, axis=0)

max_value = np.max(data)

min_value = np.min(data)

mean_value = np.mean(data)

## Print the results
print("Row wise sum is ", row_sum)
print("Column wise sum is ", col_sum)
print("Maximum value is ", max_value)
print("Minimum value is ", min_value)
print("Mean Value is ", mean_value)
