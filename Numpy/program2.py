#creating array
import numpy as np
arr=np.array([10,20,30,40])
print(arr)

#create 3*4 zero matrix
arr1=np.zeros((3,4))
print(arr1)

#create a 2*3 matrix containing only ones
arr2=np.ones((2,3))
print(arr2)

#create even numbers from 2 to 20
even=np.arange(2,20,2)
print(even)

#create 6 equally spaced numbers between 1 to 10
arr3=np.linspace(1,10,6)
print(arr3)

#create a 4*4 identity matrix
arr4=np.eye(4)
print(arr4)