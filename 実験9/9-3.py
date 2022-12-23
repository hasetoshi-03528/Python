import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
im=np.array(Image.open("./ex8-6.jpg"))
n=int(im.size/3)
hd=256*[0]
row=im.shape[0]
col=im.shape[1]
for i in range(row):
    for j in range(col):
        v=im[i,j,0]*0.299+im[i,j,1]*0.587+im[i,j,2]*0.114
        hd[int(v)]+=1
        #hd[i*col+j]=v
#plt.hist(hd,256,color='k')
bar_width=1
index=range(256)
plt.bar(index,hd,bar_width,alpha=1,color='k')
plt.show()
