from statistics import mean
from  scipy import stats

Estimates=[]

for i in range(1,76):
    Estimates.insert(i,i*10)

Estimates.sort()

#method1
#tv=int(0.1*len(Estimates))
#Estimates=Estimates[tv:]
#Estimates=Estimates[:len(Estimates)-tv]
#print(mean(Estimates))


#method2

m=stats.trim_mean(Estimates,0.1)
print(m)


#for i in range(len(Estimates)):
 #   print(Estimates[i])




