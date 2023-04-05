# NumPy Tutorial
import numpy as np

list1 = [1, 2, 3]
array1 = np.array([1, 2, 3])
print(list1)  # [1, 2, 3]
print(array1)  # [1 2 3]
# First different between list & array is [array >> Unpacking Elements]

array1 = np.array([1, 2.5, 3, 4])
print(array1)  # [1.  2.5 3.  4. ]
# Second is Array Must all elements be the same type [all output float]

# Benefits:
# Array more fast than list
# Offer math Operations on matrices
# Offer statistics operations also

# dtype attribute determine the datatype of the Array
array1 = np.array([1, 2, 3, 4], dtype="float32")
print(array1)  # [1. 2. 3. 4.]

# Zeroes & ones Arrays
array1 = np.zeros(10, dtype="int")
array2 = np.ones(10, dtype="int")
print(array1)  # [0 0 0 0 0 0 0 0 0 0]
print(array2)  # [1 1 1 1 1 1 1 1 1 1]

# 2-D Zeros & Ones Arrays

array1 = np.zeros((3, 5), dtype="int")
print(array1)
# [[0 0 0 0 0]
#  [0 0 0 0 0]
#  [0 0 0 0 0]]

# You can create Matrix in 3 or 4 or more Dimension
array1 = np.zeros((3, 5, 2, 4), dtype="int")
print(array1)

# Any Value or Array
array1 = np.full((3, 4), 3.14)
print(array1)
# [[3.14 3.14 3.14 3.14]
#  [3.14 3.14 3.14 3.14]
#  [3.14 3.14 3.14 3.14]]

# Create Array in Range
array1 = np.arange(0, 10)
print(array1)  # [0 1 2 3 4 5 6 7 8 9]

# Create Array in Range [default start = 0]
array1 = np.arange(10)
print(array1)  # [0 1 2 3 4 5 6 7 8 9]

# Create Array in Range with step size
array1 = np.arange(0, 20, 2)
print(array1)  # [ 0  2  4  6  8 10 12 14 16 18]

# Create Array with Random Elements between (0 : 1) :
array1 = np.random.random((3, 3))
print(array1)
# [[0.59843386 0.567184   0.93265006]
#  [0.6313945  0.40038906 0.48124954]
#  [0.49761184 0.51442482 0.99411807]]

# Create Array with Random Elements but normal distribution:
array1 = np.random.normal(0, 1, (3, 3))  # [1 is mean, 3 is variance]
print(array1)
# [[ 1.11893306 -0.15063746  0.61778381]
#  [ 0.27574819 -0.04094748 -1.46619869]
#  [-0.43030399  0.19351541 -0.50513429]]

# Create Array with Random integers:
array1 = np.random.randint(0, 10, (3, 3))
print(array1)
# [[7 0 9]
#  [8 5 9]
#  [4 5 3]]

# Create identity matrix
array1 = np.eye(4)
print(array1)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

# Create empty Array:
array1 = np.empty((2, 3))
print(array1)
# [[6.24649640e-312 6.24644453e-312 6.24644453e-312]
#  [6.24644454e-312 6.24644450e-312 6.24644454e-312]]

# Array Attributes
array1 = np.zeros((3, 4, 5))
print(f"dim = {array1.ndim}, and Shape is {array1.shape}, and size is {array1.size}")
print(f"Datatype of Array is : {array1.dtype}")
# Output: dim = 3, and Shape is (3, 4, 5), and size is 60
#         Datatype of Array is : float64

# Array Indexing:
array1 = np.array([1, 3, 5, 7])
print(array1[2])  # 5

# 2D Array Indexing & above:
array1 = np.array([[1, 3, 5, 7], [2, 4, 6, 8], [0, 3, 6, 9]])
print(array1[1, -1])  # 8

# Array Slicing: Accessing Sub-arrays [Like Matlab]
array1 = np.random.randint(2, 20, 20)
print(array1)  # [ 4  5 14  5 11 10 14 14  7 13 17 19 14  8  2 15  9  5 10  5]
print(array1[1:12:2])  # [ 5  5 10 14 13 19]

# Accessing array rows and columns:
array1 = np.array([[12, 5, 2, 4], [7, 6, 8, 8], [1, 6, 7, 7]])
print(array1[0, :])  # access row :  [12  5  2  4]
print(array1[0])  # access row :  [12  5  2  4]
print(array1[:, 0])  # access column :   [12  7  1]

# Sub-arrays as no-copy views
array1 = np.array([[12, 5, 2, 4], [7, 6, 8, 8], [1, 6, 7, 7]])
array1_sub = array1[:2, :2]
print(array1_sub)
array1_sub[0, 0] = 99
print(array1_sub)
print(array1)
# Change in array1 or array1_sub happen in both

# Sub-arrays as copy views
array1 = np.array([[12, 5, 2, 4], [7, 6, 8, 8], [1, 6, 7, 7]])
array1_sub = array1[:2, :2].copy()
print(array1_sub)
array1_sub[0, 0] = 99
print(array1_sub)
print(array1)
# Change in array1 or array1_sub does not depend on each others

# Reshaping of array
array1 = np.array([12, 5, 2, 4, 7, 6, 8, 8, 1, 6, 7, 7]).reshape((6, 2))
print(array1)

# row vector via reshape
array1 = np.array([1, 2, 3])
print(array1.reshape((1, 3)).shape)

# Array Concatenation
array1 = np.array([1, 2, 3])
array2 = np.array([3, 2, 1])
print(array1)
print(array2)
print(np.concatenate([array1, array2]))
print(np.concatenate((array1, array2)))

# concatenate along the first axis
array1 = np.full((2, 3), 1)
array2 = np.full((2, 3), 9)
print(np.concatenate([array1, array2], axis=0))
# [[1 1 1]
#  [1 1 1]
#  [9 9 9]
#  [9 9 9]]
print(np.concatenate([array1, array2], axis=1))
# [[1 1 1 9 9 9]
#  [1 1 1 9 9 9]]


