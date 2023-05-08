"""import numpy as np
np.arr=([])
a=int(input( ))
i=0
for i in range(a):
    x=int(input())
    np.arr.append(x)
print(np.arr)

list=[]
a=int(input( ))
i=0
for i in range(a):
    x=int(input( ))
    list.append(x)
print(list)"""
n = 3

d = dict(input("Enter key and value: ").split() for _ in range(n))

print(d)