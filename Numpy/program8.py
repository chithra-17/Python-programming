import numpy as np

arr=np.array([15,42,8,63,27,91,34,56])
#find the shape
print(np.shape(arr))
#find the size
print(np.size(arr))
#find max value
print(np.max(arr))
#find the index of max value
print(np.argmax(arr))
#sort the array
print(np.sort(arr))
#find all value greater than 40
print(arr[arr>40])
#find all even num
print(arr[arr%2==0])
#find the mean
print(np.mean(arr))
#find the minimum value
print(np.min(arr))
#reverse the array
print(arr[::-1])
