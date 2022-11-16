import numpy as np
import pandas as pd

with open ('JJ.txt','w',encoding='UTF-8') as f1:
    data = input("[输入格式:(工号,姓名,奖金)]:\n")
    c = 0
    while data!="" and c<10:
        c+=1
        f1.write(data+'\n')
        data = input()

data_rd = pd.read_table("JJ.txt",sep=',',names=["ID","name","JJ",],encoding='UTF-8')
data_sort = data_rd.sort_values(by='JJ')
data_sort.to_csv("NewJJ.txt",header=None,index=None,sep=',',encoding='UTF-8')