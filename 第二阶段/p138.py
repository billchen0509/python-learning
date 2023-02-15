import json
from pymysql import Connection
# 构建链接
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='thchj123',
)
# 构建游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('py_sql')
cursor.execute("select * from orders")
# 得到全部数据
data_tuple = cursor.fetchall()

# 打开一个txt文件
f = open('D:/11.txt','a',encoding='UTF-8')
# 将数据封装
data_dict = {}
for r in data_tuple:
    data_dict['date'] = str(r[0])
    data_dict['order_id'] = r[1]
    data_dict['money'] = int(r[2])
    data_dict['province'] = str(r[3])
    # 再把数据写入txt文件中
    f.write(json.dumps(data_dict,ensure_ascii=False))
    f.write('\n')

# 关闭
f.close()
conn.close()