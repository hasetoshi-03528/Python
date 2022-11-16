x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))

if x<y and x<z:
    print(x," < ",end=' ')
    if y<z:
        print(y," < ",z)
    else:
        print(z," < ",y)
elif y<x and y<z:
    print(y," < ",end=' ')
    if x<z:
        print(x," < ",z)
    else:
        print(z," < ",x)
else:
    print(z," < ",end=' ')
    if x<y:
        print(x," < ",y)
    else:
        print(y," < ",x)