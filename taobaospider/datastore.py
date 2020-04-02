import pandas as pd
import numpy as np
import pymysql
import re

import pandas as pd
import jieba, re
from scipy.misc import imread
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pyplot as plt

导入数据
coon = pymysql.connect(
    host='localhost', user='root', passwd='123456',
    port=3306, db='taobao', charset='utf8'
    # port必须写int类型
    # charset必须写utf8，不能写utf-8
)
cur = coon.cursor()  # 建立游标
sql='select * from taobao_food'
df=pd.read_sql(sql=sql,con=coon)
#print(df.values)
df=pd.DataFrame(df)
# df=df.drop('id',axis=1)
print(pd.isnull(df).values.any())
# df = df.dropna(how='any', inplace=True) #舍弃含有任意缺失值的行
#去重
print('去重之前的形状',df.shape)
df=df.drop_duplicates(keep='first')
print('去重之后的形状',df.shape)
print(df.head())

# 提取地址信息与购买数量

def get_buy_num(buy_num):
    if u'万' in buy_num:  # 针对1-2万/月或者10-20万/年的情况，包含-
        buy_num=float(buy_num.replace("万",''))*10000
        # print(buy_num)
    elif buy_num == ' ':
        buy_num=0
    else:
        buy_num=float(buy_num)
        # print(buy_num)
    return buy_num

df['place'] = df['place'].replace('','未知')#fillna("['未知']")
datasets = pd.DataFrame()
for index, row in df.iterrows():
    #print(row["place"])
    row["place"] = row["place"][:2]
    if row["buy_num"] == '':continue
    row["buy_num"]=get_buy_num(row["buy_num"][:-3].replace('+',''))
    #print(row["place"])

df.to_csv('taobao_food.csv',encoding='utf8',index_label=False)

####################分词，云图绘制####################
fr = open('baidu_stopwords.txt', 'r',encoding='UTF-8')
stop_word_list = fr.readlines()
new_stop_word_list = []
for stop_word in stop_word_list:
    stop_word = stop_word.replace('\ufeef', '').strip()
    new_stop_word_list.append(stop_word)
file1 = df.loc[:,'title'].dropna(how='any')  # 去掉空值
print('去掉空值后有{}行'.format(file1.shape[0]))  # 获得一共有多少行
print(file1.head())
text1 = ''.join(i for i in file1)  # 把所有字符串连接成一个长文本
responsibility = re.sub(re.compile('，|；|\.|、|。'), '', text1)  # 去掉逗号等符号
wordlist1 = jieba.cut(responsibility, cut_all=True)
print(wordlist1)
word_dict={}
word_list=''

for word in wordlist1:
    if (len(word) > 1  and not word in new_stop_word_list):
        word_list = word_list + ' ' + word
        if (word_dict.get(word)):
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1

print(word_list)
print(word_dict) #输出名字 词语出现的次数

#按次数进行排序
sort_words=sorted(word_dict.items(),key=lambda x:x[1],reverse=True)
print(sort_words[0:101])#输出前0-100的词


font_path = r'C:\Windows\Fonts\SIMYOU.TTF'

#bgimg=imread(r'1.png')#设置背景图片
wc = WordCloud(font_path=font_path,  # 设置字体
               background_color="black",  # 背景颜色
               max_words=300,  # 词云显示的最大词数
               # stopwords=stopwords,  # 设置停用词
               max_font_size=400,  # 字体最大值
               random_state=42,  # 设置有多少种随机生成状态，即有多少种配色
               width=2000, height=1720,
               margin=4,  # 设置图片默认的大小,margin为词语边缘距离
               ).generate(str(word_list))
#image_colors = ImageColorGenerator(bgimg)  # 根据图片生成词云颜色
plt.imshow(wc)
plt.axis("off")
plt.savefig("examples.jpg")  # 必须在plt.show之前，不是图片空白
plt.show()


