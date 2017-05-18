import tushare as ts
#获取大盘指数实时行情列表
df=ts.get_index()
print(df)