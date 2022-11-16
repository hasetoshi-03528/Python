import random
def MyFun(x):
    a=[]
    for i in range (0,len(x)):
        if(x[i]<60):
            a.append(1)
        elif x[i]<70 and x[i]>=60:
            a.append(2)
        elif x[i]<80 and x[i]>=70:
            a.append(3)
        elif x[i]<90 and x[i]>=80:
            a.append(4)
        elif x[i]<=100 and x[i]>=90:
            a.append(5)
        else:
            continue
    return a

x=[]
for i in range(0,30):
    num=random.randint(1,100)
    x.append(num)

print(x)
print(MyFun(x))