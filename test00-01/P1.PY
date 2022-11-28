import random
def fun(x,mark):
    num=0
    if mark==1:
        for a in x:
            if a>=0:
                num=num+1
    else:
        for a in x:
            if a<=0:
                num=num+1
    return num #此行有错误，已经改正。
x=[]
for i in range(30):
    a=random.uniform(-50,50)
    x.append(a)
result=fun(x,mark=1) #此行有错误，已经改正。
print("符合要求的数据个数:",result)
x.sort(reverse=True)
i=0
for a in x:
    print("{:8.1f}".format(a),end="")#此行有错误，已经改正。
    i=i+1
    if i%5==0:
        print ("")