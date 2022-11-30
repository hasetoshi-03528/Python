class Person:
    def __init__(self,na,ag):
        self.Name=na
        self.Age=ag
    def Disp(self):
        print("姓名:",end="")
        print(self.Name)
        print("年龄:",end="")
        print(self.Age,"岁")

class Teacher(Person):
    def __init__(self,na,ag,na_id,wo_ag):
        Person.__init__(self,na,ag)
        self.No=na_id
        self.Ta=wo_ag
    def NewDisp(self):
        Person.Disp(self)
        print("此人工号为：",end="")
        print(self.No)
        print("此人教龄为：",end="")
        print(self.Ta,"年")

na=input("姓名:")
ag=int(input("年龄:"))
na_id=input("工号:")
wo_ag=int(input("教龄:"))
t=Teacher(na,ag,na_id,wo_ag)
print("\n")
t.NewDisp()
