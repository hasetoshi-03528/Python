import math
a=int(input("input a:"))
b=int(input("input b:"))
c=int(input("input c:"))
d=(b**2)-(4*a*c)
if d > 0:
    x1=((0-b)+math.sqrt(d))/2*a
    x2=((0-b)-math.sqrt(d))/2*a
    print("x1=",x1,"\nx2=",x2)
elif d==0:
    x1=((0-b)+math.sqrt(d))/2*a
    x2=((0-b)-math.sqrt(d))/2*a
    print("x1=",x1,"\nx2=",x2)
else:
    print("无实解")