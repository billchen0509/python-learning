from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
# 读取数据
f = open('D:/1960-2019全球GDP数据.csv','r',encoding='GB2312')
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一行数据
data_lines.pop(0)
# 将数据转为字典储存
# 先定义一个字典
data_dict = {}
for line in data_lines:
    year = int((line.split(',')[0])) # 年份
    country = line.split(',')[1]  # 国家
    gdp = float(line.split(',')[2]) # gdp
    # 如何判断字典里面有没有指定key？
    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])
# 创建时间对象
timeline = Timeline({'theme':ThemeType.LIGHT})

# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element:element[1],reverse=True)
    # 取出前八的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0]) # 在x轴添加国家
        y_data.append(country_gdp[1]/100000000) # 在Y轴添加gdp数据
    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis('GDP(亿)',y_data,label_opts=LabelOpts(position='right'))
    # 反转X轴和Y轴
    bar.reversal_axis()
    # 设置标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f'{year}年全球前8GDP数据')
    )
    timeline.add(bar,str(year))

# 设置自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
# 绘图
timeline.render('1960-2019全球GDP前8国家.html')
