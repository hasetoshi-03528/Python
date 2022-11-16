with open('./T1.txt', 'r', encoding='UTF-8') as f1, open('./T2.txt', 'w', encoding='UTF-8') as f2:

    c=0

    while True:
        data1 = f1.readline()
        s = data1.swapcase()
        f2.write(s)
        if data1 == '':
            break
        c+=1

print("T1.txt有",c,"行")
