a=range(1,1000)
c=0
for i in a:
    if ('3' in str(i)):
        c+=1

with open ('C:\\ks\p3result.txt','w',encoding='UTF8') as f1:
    f1.write("1000以内含有3的数共有"+str(c)+"个")