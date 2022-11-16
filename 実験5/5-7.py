def list_a() :
    x=[]
    for i in range(100,1000):
        a=i%10
        b=(i//10)%10
        c=(i//100)%10
        if i==a**3+b**3+c**3:
            x.append(i)
    return x

print("水仙花数有：",list_a())

