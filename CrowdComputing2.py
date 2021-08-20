
import matplotlib.pyplot as plt
import math




l1=[]
l2=[]
i=0

for i in range(10):
    l1.insert(i,i)
i=0
for i in range(10):
    l2.insert(i,math.sqrt(81-i*i))

plt.plot(l1,l2)
plt.ylabel("Y values")
plt.xlabel("X values")
plt.show()
