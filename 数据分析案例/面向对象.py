from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import*
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader('D:/2011年1月销售数据.txt')
json_file_reader = JsonFileReader('D:/2011年2月销售数据JSON.txt')

jan_data = text_file_reader.read_data()
feb_data = json_file_reader.read_data()

# 将两个月的数据合并为一个list
all_data = jan_data + feb_data

# 进行数据计算
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # 当前日期有记录了,所以和老的记录累加
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# 进行可视化
bar = Bar(init_opts=InitOpts(theme=ThemeType.VINTAGE)) # 类对象

bar.add_xaxis(list(data_dict.keys())) # 添加x轴的数据
bar.add_yaxis('销售额',list(data_dict.values()),label_opts=LabelOpts(is_show=False)) # 添加y轴数据
bar.set_global_opts(
    title_opts=TitleOpts(title='每日销售额')
)

bar.render('每日销售额柱状图.html')