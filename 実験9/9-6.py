import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import jieba

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.figure(figsize=(10, 4))  # 窗口大小

fp1 = open('三国演义人名汇总.txt', "r", encoding='UTF-8')
fp2 = open('三国演义.txt', "r", encoding='UTF-8')

lines = fp1.readlines()

names = []
num = []

for line in lines:
    line = line.strip('\n')
    line = line.split(" ")
    for name in line:
        names.append(name)

f = fp2.read()
book = jieba.lcut(f)

for i in names:
    n = 0
    for j in book:
        if i == j:
            n = n+1
    num.append(n)

m = []
l = []

for k in range(len(num)):
    if num[k] > 100:
        m.append(names[k])
        l.append(num[k])

plt.subplot(121)
plt.bar(m, l, width=0.5, color='b')
plt.xticks(rotation=90)  # 旋转名字为竖排


words = " ".join(names)

mask = np.array(Image.open("star.jpg"))
wordcloud = WordCloud(
    font_path='C:/Windows/Fonts/simhei.ttf',
    prefer_horizontal=0.99,
    mask=mask,
    background_color="white",
    max_words=100,
    max_font_size=30).generate(words)
wordcloud.to_file("ciyun.png")

plt.subplot(122)
plt.imshow(wordcloud)
plt.axis('off')

plt.show()
fp1.close()
fp2.close()
