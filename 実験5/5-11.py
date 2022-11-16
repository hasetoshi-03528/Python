import matplotlib.pyplot as plt
from matplotlib import patches
fig, ax = plt.subplots(figsize=(4,4))
r = patches.Rectangle( (0,0) , 1.5, 1, fill=False, edgecolor="blue", linewidth=3, label="rectangle")
ax.add_patch(r)

plt.legend()
plt.show()