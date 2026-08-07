# Write A func that:
#Accepts a Numpy array.
#Returns: Max, Min, Avg


import numpy as np
def value(arr):
    return np.max(arr), np.min(arr), np.mean(arr)
    
arr=np.array([10,20,30,40,50])
Maximum, Minimum, Average=value(arr)

print("Maximum:",Maximum)
print("Minimum:", Minimum)
print("Average:", Average)

