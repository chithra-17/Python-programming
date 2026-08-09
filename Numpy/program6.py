import numpy as np
arr=np.array([1,2,3,4,5,6])
arr2=np.array([10,20,30,40])
print(arr[arr%2==0])
print(arr[(arr>1)&(arr<6)])

#sorting and searching
print(np.sort(arr))
print(np.argsort(arr))
print(np.where(arr==6))
print(np.where(arr%2==0))
