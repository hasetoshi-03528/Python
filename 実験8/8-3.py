class Rect:
    def __init__(self,y,x):
        self.__len=y
        self.__wid=x
    def P(self):
        return (self.__len+self.__wid)*2
    def S(self):
        return self.__len*self.__wid
    def S_sum(self,s_2):
        return self.S()+s_2.S()

(y1,x1)=eval(input("第一个矩形的长和宽(y,x):"))
(y2,x2)=eval(input("第二个矩形的长和宽(y,x):"))
r1=Rect(y1,x1)
r2=Rect(y2,x2)
print("第一个矩形周长:",r1.P())
print("第一个矩形面积:",r1.S())
print("两个矩形面积和:",r1.S_sum(r2))
