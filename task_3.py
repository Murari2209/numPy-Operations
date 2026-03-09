## numpy mathematical formulas
import numpy as np

## Create a NumPy array of values
values = np.array([2, 4, 6, 8, 10])

## Perform mathematical operations on the array and round the results to 2 decimal places
sqrt_values = np.round(np.sqrt(values), 2)

exp_values = np.round(np.exp(values), 2)

log_values = np.round(np.log(values), 2)

total_sum = np.round(np.sum(values), 2)

cumulative_sum = np.round(np.cumsum(values), 2)

## Print the results
print("Square roots:", sqrt_values)
print("Exponentials:", exp_values)  
print("Logarithms:", log_values)
print("Total sum:", total_sum)
print("Cumulative sum:", cumulative_sum)

