a=9
x='A'
for i in range(a):
    for j in range(i):
        print(' ',end='')
    for j in range((a-i)*2):
        print(x,end='')
    print()
    x=chr(ord(x)+1)