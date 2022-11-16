x=int(input("请输入年份:"))
if x%4 == 0 and x%100 != 0 or x%400 ==0:
    print(x,"是闰年")
else:
    print(x,"不是闰年")