from pymysql import Connection
from data_define import *
from file_define import *
from pymysql import Connection

text_file_reader = TextFileReader('D:/2011年1月销售数据.txt')
json_file_reader = JsonFileReader('D:/2011年2月销售数据JSON.txt')

jan_data = text_file_reader.read_data()
feb_data = json_file_reader.read_data()
# 合并两个月的数据为一个list
all_data = jan_data + feb_data

# 构建sql链接对象
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='thchj123',
    autocommit=True
)
# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('py_sql')
# 组成sql语句
for record in all_data:
    sql = f"insert into orders(order_date,order_id,money,province) values('{record.date}','{record.order_id}','{record.money}','{record.province}')"
    # 执行sql语句
    cursor.execute(sql)
# 关闭
conn.close()