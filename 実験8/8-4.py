class Person:
    def __init__(self,na,ag):
        self.Name=na
        self.Age=ag
    def Disp(self):
        print("姓名:",end="")
        print(self.Name)
        print("年龄:",end="")
        print(self.Age,"岁")

na=input("姓名：")
ag=int(input("年龄："))
p=Person(na,ag)
print("\n")
p.Disp()
