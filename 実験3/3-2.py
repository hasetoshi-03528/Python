x=int(input("x="))
if x<1000:
    y=x
elif x>=1000 and x<2000:
    y=0.9*x
elif x>=2000 and x<3000:
    y=0.8*x
else :
    y=0.7*x
print("y=",y)