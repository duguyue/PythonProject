import tushare as ts

#print(ts.__version__);

df=ts.get_k_data('002743')
print(df)