x=int(input("请输入成绩:"))

if x<60:
    print("绩点:0")
elif x<70 and x>=60:
    print("绩点:2")
elif x<80 and x>=60:
    print("绩点:3")
elif x<90 and x>=80:
    print("绩点:4")
else:
    print("绩点:5")