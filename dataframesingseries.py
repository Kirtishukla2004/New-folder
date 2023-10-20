import pandas as pd
import numpy as np 
dic={ 'Name':['raj ','aman','ritu','ajay'],
       'eng':[50,40,50,30],
       'maths':[60,50,40,30],
       'science':[80,50,50,40]
    }
data=pd.DataFrame(dic)
print("labels",data.keys())
print("row label",data.index)
print(data.columns)
print(data.shape[0])
print(data.shape[1])
print(data.size)
transpose=data.T
print(transpose)
print(data[['eng','Name']])
print(data.loc[0:1,['Name','eng','maths']])
data.loc[len(data)]=['ravi',45,67,89]
print(data)
data['percentage'] = [60, 50, 60, 50]
print(data)