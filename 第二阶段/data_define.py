'''
数据定义的类
'''

class Record:
    # 定义四个成员变量（参照文件内容）
    # 构造方法构建成员变量 __init__
    def __init__(self,date,order_id,money,province):
        self.date = date # 订单日期
        self.order_id = order_id # 订单号
        self.money = money # 订单金额
        self.province = province # 订单省份

    def __str__(self):
        return f'{self.date},{self.order_id},{self.money},{self.province}'