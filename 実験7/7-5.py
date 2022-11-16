with open('./T1.txt', 'r', encoding='UTF-8') as f1, open('./T2.txt', 'r', encoding='UTF-8') as f2, open('./T3.txt', 'a', encoding='UTF-8') as f3:
    data1=f1.read()
    f3.write(data1+'\n')
    data2=f2.read()
    f3.write(data2)
