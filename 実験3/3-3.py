x=int(input("上网时间:"))
if x<10:
    y=30
elif x<50 and x>=10:
    y=30+2.5*(x-10)
else:
    y=30+2.5*40+2*(x-50)

if y>150:
    y=150

print("本月网费:",y)