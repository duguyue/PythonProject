sites = ["Baidu","Google","Taobao"]
for site in sites:
    if site == "Google":
        print("谷歌搜索!")
        break
    print("循环数据 "+site)
else:
    print("没有循环数据!")
print("完成循环!")