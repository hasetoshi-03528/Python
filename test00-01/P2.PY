import random
strs = list(input("1.请输入一组数据(用逗号分隔)：")) #此行有错误，已经改正
s,t=eval(input("2.输入随机系数a取值区间的上下界s和t："))
lst=strs#.split()
print("激活函数值如下：")
a=random.uniform(s,t) #此行有错误，已经改正
for item in range(len(lst)):
    x=float(item)
    if x>0:#此行有错误，已经改正
        y=x
    else:
        y=a*x
    print("y={:.3f}".format(y))