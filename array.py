import array
import numpy as np

# Basic numpy operation
#Create an array
numbers = np.array([1, 2, 3, 4, 5, 6])
print(numbers)

#Create a 2D array (matrix of numbers )
nums = np.array([[1,2,3],[4,5,6],[7,8,9]])
nums[1,1] = 1000000000
nums[2,2] = -999999999
print(nums)

print("shape of nums",nums.shape) #output 