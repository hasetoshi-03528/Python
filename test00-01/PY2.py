s=0
i=0
a=0
d=10**(-5)
while 1:
    a=1/(2+3*i)
    if abs(a)<d:
        break
    else:
        s+=a
        i+=1
        continue

print(s)