

def Bubble(a):
    n=len(a)

    for i in range(n):
        for j in range(0,n-1-i):
            if(a[j]>a[j+1]):
               temp=a[j]
               a[j]=a[j+1]
               a[j+1]=temp







a=[5,1,4,2,3]

Bubble(a)

print(a)