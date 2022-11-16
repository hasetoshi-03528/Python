str=input("输入表达式：")
m=0
n=0
for i in str:
    if(i=='('):
        m=m+1
    if(i==')'):
        n=n+1
if(m<n):
    print("右括号多于左括号")
elif(m>n):
    print("左括号多于右括号")
else:
    print("括号使用正确")