import numpy as np

arr = np.array([[1, 2, 3], [2, 3, 4]])
print(np.version)
print(arr)

arr1 = np.array([[1, 2], [2, 3], [4, 5]])
print(arr1)
arr2 = np.matmul(arr, arr1)
print(arr2)
arr3 = np.array([[1], [2], [3]])
print(arr3.reshape(1, -1))
zmat = np.zeros((5,5))
print(zmat)


d = np.full((3, 3), 6, dtype = 'complex')
print(d)