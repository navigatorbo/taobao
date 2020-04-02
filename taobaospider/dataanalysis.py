import pandas as pd
import numpy as np
from pyecharts import Map

df = pd.read_csv("F:/python/python_file/Spider/taobaospider/taobao_food.csv")
# print(df['buy_num'].sort_values(ascending=False))
# print(df.loc[df['buy_num'].sort_values(ascending=False).index,'shop'])
# a=df['buy_num'].sort_values(ascending=False)
# b=df.loc[df['buy_num'].sort_values(ascending=False).index,'shop']
# c=df.loc[df['buy_num'].sort_values(ascending=False).index,'title']
# frames = [a,b,c]
# data=pd.concat(frames,axis=1)
# print(data)

a=df['buy_num'].sort_values(ascending=False)
b=df.loc[df['buy_num'].sort_values(ascending=False).index,'place']
c=df.loc[df['buy_num'].sort_values(ascending=False).index,'shop']
frames = [a,c,b]
data=pd.concat(frames,axis=1)
print('销售排名商店与所在城市信息分布\n',data)

buy_num_sum=df.groupby(['place'])['buy_num'].sum().sort_values(ascending=False)
print('地区销售总量信息分布\n',buy_num_sum)

brougt=buy_num_sum.values.tolist()
address=buy_num_sum.index.tolist()

map = Map("地区销售总量信息分布", "data from 51job",title_color="#404a59", title_pos="left")
map.add("销售总量", address,brougt , maptype='china',visual_range=[0, 300000],is_visualmap=True,visual_text_color='#000',is_label_show=True,is_map_symbol_show=False)
map.render("地区销售总量信息分布图.html")
