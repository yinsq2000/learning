import numpy as np
# print(np.__version__)
'''
identity = np.eye(3)
print(identity)

matrix = np.array([[1,2],[3,4]])
print(matrix)
transposed = matrix.T
print(transposed)

full = np.full((2, 3), 7)
print(full)

arr = np.array([10, 20, 30, 40, 50])
element = arr[2] # 获取第三个元素 (30)
print(element)
slice = arr[1:4] # 获取 [20, 30, 40]
print(slice)
matrix = np.array([[1,2,3],[4,5,6]])
print(matrix)
row = matrix[0, :] # 获取第一行 [1 2 3]
col = matrix[:, 1] # 获取第二列 [2 5]
print(row)
print(col)

arr = np.arange(6)
print(arr)
reshaped = arr.reshape(2, 3) # 变为2行3列的数组
print(reshaped)

matrix = np.array([[1,2],[3,4]])
transposed = matrix.T

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.dot(a, b))
v_stack = np.vstack((a, b)) # 垂直堆叠
h_stack = np.hstack((a, b)) # 水平堆叠
print(v_stack)
print(h_stack)

arrange = np.arange(0, 100, 2)
print(arrange)

arr3 = np.ones((2,3),dtype=int)
print(arr3)
print(arr3.dtype)
'''
arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])

# 1. 取第2行（索引1）
print(arr[1, :])    # [5 6 7 8]
arr1 = arr[1, :]
arr1[2] = 10
print(arr1)
# 2. 取第3列（索引2）
print(arr[:, 2])    # [ 3  7 11]

# 3. 前2行，后2列
print(arr[:2, 2:])
# [[3 4]
#  [7 8]]

# 4. 隔行取，所有列
print(arr[::2, :])
# [[ 1  2  3  4]


