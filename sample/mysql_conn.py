import pymysql

conn=pymysql.connect(user='root',passwd='',host='localhost',db='affairmanage')
cur=conn.cursor()
cur.execute("SELECT * FROM `user`")
for r in cur:
    print("row_number:",(cur.rownumber))
    print("Id:"+str(r[0])+" username:"+str(r[1])+" age:"+str(r[2]))
cur.close()
conn.close()