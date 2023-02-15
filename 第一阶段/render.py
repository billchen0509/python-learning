"""
可视化数据
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts,TooltipOpts,LabelOpts
# 处理数据
f_us = open('D:/美国.txt','r',encoding='UTF-8')
us_data = f_us.read() # 美国的数据

f_jp = open('D:/日本.txt','r',encoding='UTF-8')
jp_data = f_jp.read() # 日本的数据

f_india = open('D:/印度.txt','r',encoding='UTF-8')
india_data = f_india.read() # 印度的数据

# 去掉不合json规范的开头
us_data = us_data.replace('jsonp_1629344292311_69436(','')
jp_data = jp_data.replace('jsonp_1629350871167_29498(','')
india_data = india_data.replace('jsonp_1629350745930_63180(','')
# # 去掉不合json规范的结尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
india_data = india_data[:-2]
# json转python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(india_data)
# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']
# 获取日期数据，用于x轴，取2020年，到314下标结束
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]
# 获取确认数据，用于Y轴，取2020年，到314下标结束
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成图表
line = Line() # 构建折线图对象
# 添加X轴数据
line.add_xaxis(us_x_data) # x轴是统一的
# 添加Y轴数据
line.add_yaxis('美国确诊人数',us_y_data,label_opts=LabelOpts(is_show=False))  # 美国的确认数据
line.add_yaxis('日本确认人数',jp_y_data,label_opts=LabelOpts(is_show=False))  # 日本的确诊数据
line.add_yaxis('印度确诊人数',in_y_data,label_opts=LabelOpts(is_show=False))  # 印度的确诊数据

# 设置全局选项
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title='2020年美日印三国确诊人数折线图',pos_left='center',pos_bottom='1%'),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True),
)

# 调用render方法，生成图表
line.render()
# 关闭文件对象
f_us.close()
f_jp.close()
f_india.close()
