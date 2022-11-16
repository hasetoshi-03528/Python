from functools import reduce
from pip._vendor.distlib.compat import raw_input

Tn = 0
Sn = []
n = int(raw_input('n = :'))
a = int(raw_input('a = :'))
print("s=", end="")
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn,end="+")
Sn = reduce(lambda x, y: x + y, Sn)
print("\b=",end="")
print(Sn)