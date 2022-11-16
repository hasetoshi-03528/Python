def factorial(num):
    val=1
    for i in range(num,1,-1):
        val*=i
    return val

def pow(a,b):
    return a**b

x=int(input("x="))
s=0
t=0
i=1
while 1:
    t=pow(x,i)/factorial(i)
    if(abs(t)<pow(10,-6)):
        break
    else:
        s+=t
        i+=2

print(s)