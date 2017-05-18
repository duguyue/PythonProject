import numpy as np
import pandas as pd
import tushare as ts
"""
a=np.random.standard_normal((9,4))
b=pd.DataFrame(a)
b.columns=[['num1','num2','num3','num4']]

h5=pd.HDFStore('/data/stock/test1.h5','w')
h5['data']=b
h5.close()
"""

'''
df=ts.get_k_data('002743')
print(df)
df.to_hdf('e:/day/hdf.h5','002743')
'''

df=ts.get_hist_data('000875')
store=HDFStore('e:/day/store.h5')
store['000875']=df
store.close()