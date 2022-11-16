def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

x=int(input("n="))
for i in range(1,x+1):
    print(fibonacci(i))
