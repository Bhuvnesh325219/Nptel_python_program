

import numpy as np

a=np.array([1,2,5])
b=np.array([[4,5,6],[7,8,9]])

#print(type(a))
#print(a.dtype)
#print(type(b))
#print(b.dtype)


#print(a.shape)
#print(b.shape)

b=np.zeros((3,3))
c=np.ones((4,4))
d=np.full((3,3),7)
e=np.random.random((2,2))

#print(b)
#print(c)
#print(d)
#print(e)

x=np.array([1,2],dtype=np.int64)

#print(x.dtype)


x=np.array([[1,2],[3,4]])
y=np.array([[1,1],[2,2]])

print(x|y)
print(x&y)
print(x+y)
print(x*y)
print(np.sqrt(x))



