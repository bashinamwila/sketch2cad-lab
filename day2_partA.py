import numpy as np
a=np.array([[0,1,0,1,0,1],[0,1,0,1,0,1],[0,1,0,1,0,1],[0,1,0,1,0,1],[0,1,0,1,0,1],[0,1,0,1,0,1]])
print(a.ndim)
print(a.size)
print(a[0])
print(a[:,-1])
print(a[1:, 1:3])
a[0,:]=99
print(a)