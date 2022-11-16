import numpy as np
import pandas as pd

data_rq = pd.read_table("学生成绩文件.txt",sep='\t', names=["ID","Name","Grade"], encoding="UTF-8")
grade_max = data_rq['Grade'].max()
grade_min = data_rq['Grade'].min()
grade_mean = data_rq['Grade'].mean()

print("最高分是",grade_max)
print("最低分是",grade_min)
print("平均分是",grade_mean)
"""f1=open('学生成绩文件.txt','r', encoding='UTF-8')
stu=f1.readlines()
score=[]
for s in stu:
    m=s.split(" ")
    score.append(int(m[2]))
print(score)
ma=max(score)
mi=min(score)
s=sum(score)
avg=s/len(score)
print (ma)
print (mi)
print (s)
print (avg)"""
