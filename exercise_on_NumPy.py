import pandas as pd
import numpy as np

df = pd.read_csv("500_Person_Gender_Height_Weight_Index.csv")
print(df.head())
df.info()
data = df.iloc[:, -3:].values
print(data)
print(f"type: {type(data)}")

# 1- Find the number of dimensions, the size and the shape of this array
print(f"Dim: {data.ndim}")
print(f"size: {data.size}")
print(f"Shape: {data.shape}")

# 2- What is the data type of this array?
print(f"DataType: {data.dtype}")

# 3- Return the target value of the 500 observations
target = data[:, -1]
print(target)

# 4- Extract every 3 observations of the data
print(data[::3, :])
# 5- Extract the first and last columns in one array. (using hstack)
col1 = data[:, 0].reshape(-1, 1)
col3 = data[:, 2].reshape(-1, 1)
print(np.hstack((col1, col3)))

# 6- Reverse the array (the last observation becomes the first)
print(data[::-1, :])

# 7- What is the maximum and minimum height?
max_height = np.max(data[:, 0])
min_height = np.min(data[:, 0])
print(f"max height: {max_height} cm")
print(f"min height: {min_height} cm")

# 8- What is the maximum and minimum weight?
max_weight = np.max(data[:, 1])
min_weight = np.min(data[:, 1])
print(f"max weight: {max_weight} cm")
print(f"min weight: {min_weight} cm")

# 9- Find the mean and standard deviation of height using the simple operations only. (np.sum)
heights = data[:, 0]
sum_data = heights.sum()
mean_data = sum_data/len(heights)
print(f"mean is: {mean_data} ")

x = heights - mean_data
x = x**2
x = x.sum()
y = np.sqrt(x/len(heights))
print(f"Standard deviation: {y}")

# 10
print(f"Mean: {np.mean(heights)} Standard Deviation: {np.std(heights)}")
# 11
print(f"{np.percentile(heights,[25, 50, 75])} median: {np.median(heights)}")

# 12 normalize
Norm_height = (heights-np.mean(heights))/np.std(heights)
# print(Norm_height)

# 13 normalize with min max scaler
norm = (heights-np.min(heights))/(np.max(heights)-np.min(heights))
print(norm)

# 14
print(f"index of tallest: {np.argmax(heights)}")
