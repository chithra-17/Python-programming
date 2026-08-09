#Joining and splitting

import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.concatenate((a,b)))
d=np.vstack((a,b))
c=np.hstack((a,b))
print(c)
e=np.vstack((c))
print(np.split(c,3))
print(np.concatenate((c,d),axis=0))
print(np.concatenate((c,d),axis=1))
