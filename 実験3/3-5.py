m=int(input("总数:"))
n=int(input("总脚数:"))
while n%2!=0:
    n=int(input("请重新输入总脚数:"))

y=n/2-m
x=m-y

print("鸡为",x,"只")
print("兔为",y,"只")

if x<0 or y<0:
    print("ERROR: 由于输入的脚的数量小于总数量所以答案为负数")