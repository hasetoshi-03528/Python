class mobi:
    def __init__(self,sn,distance,day):#此处有错误
        self.sn=sn
        self.distance=distance
        self.day=day
    def getavDis(self):#此处有错误
        avdis=self.distance/self.day
        return avdis
m1=mobi('20160001',3900000,722)
m2=mobi('20171071',82000,402)
m3=mobi('20180041',72000,181)
li=[]
li.append(m1)
li.append(m2)
li.append(m3)
allAver=0
for bi in li:
    allAver+=bi.getavDis()#此处有错误
allAver /=len(li)
print(allAver)