import random
num=random.randint(1,100)
c=1
while 1:
    x=int(input("输入猜测的数:"))
    if x == num:
        print(x,"恭喜你猜对了! 你猜了",c,"次")
        break
    elif c==5:
        print("答案是",num)
        print("游戏失败")
        break
    elif x>num:
        print(x,"大了")
        print("还有",5-c,"次")
        c+=1
        continue
    elif x<num:
        print(x,"小了")
        print("还有",5-c,"次")
        c+=1
        continue