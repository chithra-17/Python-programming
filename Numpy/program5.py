#Reshaping
import numpy as np
arr=np.array([1,2,3,4,5,6])
arr2=arr.reshape(2,3)
print(arr2)
print(arr2.T)
print(arr.reshape(2,-1))
print(arr.reshape(-1,2))
print(arr2.flatten())
print(arr2.ravel())