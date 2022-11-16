import random
import numpy as np

x=np.empty(50)

for i in range(5):
    for j in range(10):
        a=random.uniform(-1,1)
        x[i*j]=a

x=x.reshape(5,10)
print("001\n",x)
_x=x.T
print("002\n",_x)
print("003\n",np.dot(_x, x))