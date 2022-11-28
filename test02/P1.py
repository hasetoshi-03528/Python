import numpy as np
import pandas as pd

with open ('C:\\ks\New_Data.csv','w',encoding='UTF8') as f1:
    data_rq = pd.read_csv("Data.csv",sep=',',encoding="UTF-8")
    czz_max = data_rq['成长值'].max()
    czz_min = data_rq['成长值'].min()
    czz_mean = data_rq['成长值'].mean()
    f1.write('最高成长值,最低成长值,平均成长值'+'\n'+str(czz_max)+','+str(czz_min)+','+str(czz_mean))