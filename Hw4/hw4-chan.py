import math
import matplotlib.pyplot as plt

m=1.0
n=8.0

arr = []
for k in range(1,21):
    temp = (1-math.exp((-k*m)/n))**k
    arr.append(round(temp,4))
    print "k:",k,"-",round(temp,4)

plt.plot(arr)
plt.xlabel('number of hash functions,k')
plt.ylabel('probability of false positive')
plt.show()
