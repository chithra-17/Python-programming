#2D indexing and slicing

import numpy as np

arr=np.array([[10,20,30],
             [40,50,60],
             [90,70,80]])

print(arr[0]) #print row 1
print(arr[0:3,1:2]) #print 2nd column
print(arr[2]) #print 3rd row
print(arr[0:2]) #print first 2 row
print(arr[1:3]) #print last 2 rows
print(arr[0:2,1:3]) #print sub array

