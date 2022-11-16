import random
print("(a)")
n=random.randint(5,10)
x = 'a'
for i in range(1,n):
    for j in range(1,n-i):
        print(end=" ")
    for k in range(0,i*2-1):
        print(x,end="")
    print(end="\n")
    x=chr(ord(x)+1)

print()

print("(b)")
#n=random.randrange(5,10,2)
x='A'
row = n
column = n
start = int(n/2)
end = int(n/2)
for i in range(0, row, 1):
    for j in range(0, column, 1):
        if j >= start and j <= end:
            print(x, end="")
        else:
            print(" ", end="")
    print("")
    x=chr(ord(x)+1)
    if i < int(n / 2):
        start = start - 1
        end = end + 1
    else:
        start = start + 1
        end = end - 1