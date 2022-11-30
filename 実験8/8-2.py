class identifier:
    def __init__(self,id):
        self.my_id=id
    def get_year(self):
        return self.my_id[6:10]
    def my_print(self):
        print(self.my_id)

in_id=input("身份证号：")
while len(in_id)!=18:
    print("身份证号格式有误")
    in_id=input("请重新输入身份证号：")
id_bir=identifier(in_id)
print("此人出生年份为：",end="")
print(id_bir.get_year())
print("此人身份证号为：",end="")
id_bir.my_print()