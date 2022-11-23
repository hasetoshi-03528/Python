class Building:
    def __init__(self,l,w,f,p):
        self.len = l
        self.wid = w
        self.flo = f
        self.pri = p

    def area(self):
        return self.len * self.wid * self.flo

    def pri_sum(self):
        return self.area()*self.pri

leng = float(input("房子宽度(m):"))
widt = float(input("房子长度(m):"))
floo = int(input("房子层数(1~):"))
pric = float(input("房子价格(元/m^2):"))

bui = Building(leng,widt,floo,pric)

print("房子面积:",bui.area(),"m^2")
print("房子总价:",bui.pri_sum(),"元")