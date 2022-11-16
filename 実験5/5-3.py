def fun(x):
    copy_number = x
    reversed_number = 0
    while x > 0:
        remainder = x % 10
        reversed_number = reversed_number * 10 + remainder
        x = x // 10
    return reversed_number

n=int(input("x="))
print(fun(n))
for i in range (1000,10000):
    if(i==fun(i)):
        print(i, end=' ')