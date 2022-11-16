num = [0, 1, 2, 3 ,4, 5, 6, 7, 8, 9]
e_num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

mydict = dict(zip(num, e_num))
str = input("电话号码:")

for i in str:
    print(mydict[int(i)], end=" ")
print()
