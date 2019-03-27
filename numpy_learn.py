
# 1 import numpy
import numpy as np
import tensorflow as tf

# # 2 print the numpy version and the configuration
# print(np.__version__)
# np.show_config()

# # 3 Create a null vector of size 10
# Z = np.zeros((3,1,4),order="C")
# print(Z)

# # 4 How to find the memory size of array
# Z = np.zeros((2,4,1),dtype=float)
# print(Z)
# print("%dbytes"%(Z.size * Z.itemsize))

# # 5 How to get the doucumentation of the numpy fuction
# np.info(np.add_newdoc_ufunc)

# # 6 Create a null vector of size 10 but fifth value which is 1
# Z = np.zeros(10)
# Z[4] = 1
# print(Z)
#
# Z = np.zeros((2,3,4))
# Z[1][2][2] = 1
# print(Z)

# # 7 Create a vector with values ranging from 10 to 49
# Z = np.arange(10,50)
# print(Z)

# # 8 Reverse a vector
# Z = np.arange(20,40)
# print(Z[::-1])

# # 9 Create a 3x3 matrix with values ranging from 0 to 8
# Z = np.arange(9).reshape(3,3)
# print(Z)

# # 10 find the non-zero elements from [1,2,0,0,4,0]
# Z = np.nonzero([1,2,0,0,4,0])
# print(np.transpose(Z))
# np.info(np.nonzero)

# # 11 Create a 3x3 identity matrix
# Z = np.eye(5)
# print(Z)

# 12 Create a 3x3x3 array with random values
Z = np.random.random((3,3,3))
print(Z)

