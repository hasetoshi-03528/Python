import matplotlib.pyplot as plt
import numpy as np
fig,ax = plt.subplots(figsize=(6,8))
plt.rcParams['axes.unicode_minus']=False
plt.ylim(0,1)
plt.subplot(211,title="Squaring Curve",xticks=np.arange(1.0))
x=-1
Y=[]
X=[]
while x<=1:
    Y.append(x**2)
    X.append(x)
    x+=0.01
plt.plot(X,Y,marker='.')

plt.subplot(212,title="Reciprocal Curve",xticks=np.arange(1.0))
plt.ylim(0,10.5)
plt.xlim(0,0.95)
x=0.1
Y=[]
X=[]
while x<=0.9:
    t=1/x
    Y.append(t)
    X.append(x)
    x+=0.01
    print(x)
    print(t)
plt.plot(X,Y,marker='.')
plt.show()
