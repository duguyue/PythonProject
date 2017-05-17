import tushare as ts

#获取股票代号为600848的所有历史数据
all_data=ts.get_hist_data('600848')
print(all_data)

#获取股票实时数据
#df=ts.get_realtime_quotes('600848')

#按日期获得股票数据
#df=ts.get_tick_data('600848',date='2017-05-10')
#print(df.head(10))