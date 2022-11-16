s=0
a=0
j=0
i=1
d=10**(-4)
while 1:
    i+=j
    a=1/i
    s+=a
    if a<d:
        print(s)
        break
    else:
        j+=1
        continue