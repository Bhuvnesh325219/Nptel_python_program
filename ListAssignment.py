

list=[int(i) for i in input().split()]

list2=[]

for item in list:
    if item not in list2:
       list2.append(item)



print(list2)
