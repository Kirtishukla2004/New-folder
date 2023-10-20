import numpy as np
import pandas as pd
data = pd.Series([1, 2, 3, 4, 5,None,None], index=['a', 'b', 'c', 'd', 'e','f','g'])
data.name="donation"
data.index.name="section"
print(data>1)

if data.isnull().any():
    data = data.fillna(5)

print(data)

