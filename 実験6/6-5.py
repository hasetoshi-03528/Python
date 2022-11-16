mylist=[]

while 1:
    t = input()
    if t=="-1":
        break
    mylist.append(t.split())

mydict=dict(mylist)

while 1:
    tmp = input()
    if tmp in mydict:
        print(tmp+" ",end="")
        print(mydict[tmp])
    elif tmp == "xxx":
        break
    else:
        print("Not found")