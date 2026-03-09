## Creating NumPy Arrays
import numpy as np

## Create a 1D array of integers from 1 to 10
oneD_array = np.arange(1, 11)

## Create a 2D array of integers from 1 to 9
twoD_array = np.arange(1, 10).reshape(3, 3)

# Create a list of integers and convert it to a NumPy array
list_array = np.array([10, 20, 30, 40, 50])

# Print the arrays shape
print("shape of 1D array:", oneD_array.shape)
print("shape of 2D array:", twoD_array.shape)
print("shape of list as array:", list_array.shape)

## Print the datatype of the arrays
print("datatype of 1D array:", oneD_array.dtype)
print("datatype of 2D array:", twoD_array.dtype)
print("datatype of list as array:", list_array.dtype)