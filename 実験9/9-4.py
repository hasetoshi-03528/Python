import matplotlib.pyplot as plt
import numpy as np

def r(a, theta):
    coef = a * (1 + np.cos(theta))
    return coef * np.cos(theta), coef * np.sin(theta)

theta = np.linspace(0, 2 * np.pi, 100)
x, y = r(3, theta)
fig1 = plt.figure(figsize=(6, 6))
ax=plt.subplot(111,title="rt")
ax.plot(x,y,marker='.')

theta_list = np.arange(0, 2*np.pi, 0.05)
r_list = 1 + np.cos(theta_list)
fig2 = plt.figure(figsize=(6, 6))
bx=plt.subplot(111,title="rt-1",projection="polar")
bx.plot(theta_list, r_list,".")
plt.show()
