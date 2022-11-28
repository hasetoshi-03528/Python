import random
import numpy as np

x=np.empty(20)
set1=0
set2=0
set3=0
for i in range(20):
    a=random.randint(0,30)
    x[i]=a
    if a<=9 and a>=0:
        set1 += 1
    elif a<=19 and a>=10:
        set2 += 1
    else:
        set3 += 1

_x=x.reshape(4,5)
print(_x)

print("0~9:",set1,"个")
print("10~19:",set2,"个")
print("20~30:",set3,"个")

x_max=max(x)
x_point = np.argmax(x)+1
if x_point<5:
    p_x = x_point
else:
	p_x=x_point-10
	if p_x>5:
		p_x = p_x-6
p_y=(x_point/5)+1
print("最高成绩是",x_max,"，索引是","(",int(p_y),",",abs(p_x),")")

y=x
y_sort=np.sort(y)
_y_sort=y_sort.reshape(4,5)
print(_y_sort)
with open ('C:\\ks\p2resule.txt','w',encoding='UTF8') as f1:
    f1.write(str(_y_sort))