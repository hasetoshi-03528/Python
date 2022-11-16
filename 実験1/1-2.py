import imp


import math
x=int(input("斜边:"))
y=int(input("一个直角边:"))
z=float(math.sqrt(x**2-y**2))
print("另一个直角边是:", z)
print("周长:", x+y+z)
print("面积:", y*z/2)