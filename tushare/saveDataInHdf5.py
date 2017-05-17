import numpy as np
import pandas as pd

a=np.random.standard_normal((9,4))
b=pd.DataFrame(a)
b.columns=[['num1','num2','num3','num4']]

#print(b)

h5=pd.HDFStore('/data/stock/test1.h5','w')
h5['data']=b
h5.close()