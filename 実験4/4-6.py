pi=0
i=0
while 1:
    if i==0:
        pi=2
    else:
        pi*=((2*i)**2)/((2*i-1)*(2*i+1))
    i+=1
    if i==1000000:
        print(pi)
        break
    else:
        continue