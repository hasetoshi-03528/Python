def fun(num):
    if num <= 1:
        return "False"
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return "False"
                break
        else:
            return "True"

m=int(input("m="))
a=fun(m)
print(a)
limit = 100
for i in range(2, limit):
    if(fun(i)=="True"):
        print(i, end=' ')