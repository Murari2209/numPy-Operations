## Percentile & Sorting

import numpy as np

## Create a NumPy array of values
marks = np.array([78,85, 90,66,72,88,95,60])

sorted_marks = np.sort(marks)

percentiles = np.percentile(marks, [25, 50, 75])  

average_marks = np.mean(marks)  

avg_count = np.sum(marks > average_marks)

## Print the results
print("Sorted marks: ", sorted_marks)
print("Percentiles (25th, 50th, 75th): ", percentiles)
print("Average marks: ", average_marks)
print("Number of students scoring above average: ", avg_count)
