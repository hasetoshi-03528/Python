import random
import numpy as np

x=np.empty(50)

for i in range(5):
    for j in range(10):
        a=random.uniform(0,1)
        x[i*j]=a

x=x.reshape(10,5)
_x=x.T

print(_x)