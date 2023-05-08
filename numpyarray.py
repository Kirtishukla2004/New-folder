import numpy as np 
a=[]
n=int(input("enter size of the array "))
for i in range(n):
    i=int(input("enter element "))
    a.append(i)
myarr=np.array(a)
print(myarr)