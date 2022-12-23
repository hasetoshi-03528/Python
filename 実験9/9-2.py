import matplotlib.pyplot as plt
import numpy as np

plt.subplots(figsize=(12,8))
plt.title("Sine Function Scatter Curve")
plt.xlim=(-4,4)
x=np.arange(-np.pi,np.pi,0.05)
y=np.sin(x)
plt.axhline(y=0,c="black")
plt.axvline(x=0,c="black")
plt.scatter(x,y,marker="*")
plt.plot((0,0),color="black")
plt.text(-np.pi,0.1,"-pi")
plt.text(np.pi,0.1,"pi")
plt.text(0.1,1,"Y")
plt.text(3.3,-0.1,"X")
plt.show()