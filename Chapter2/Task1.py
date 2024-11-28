import matplotlib.pyplot as plt
import numpy as np

v = np.array([1, 2])
w = np.array([4, -6])
vw = v + w

fig, axe = plt.subplots(figsize=(6, 6))


ax1 = plt.arrow(0, 0, v[0], v[1], head_width=0.2, width=.1, color='k', length_includes_head=True)
ax2 = plt.arrow(v[0], v[1], w[0], w[1], head_width=0.2, width=.1, color=[.5, .5, .5], length_includes_head=True)
ax3 = plt.arrow(0, 0, vw[0], vw[1], head_width=0.2, width=.1, color=[.8, .8, .8], length_includes_head=True)

plt.grid(linestyle='--',linewidth=.5)
plt.axis('square')
plt.axis([-6,6,-6,6])
plt.legend([ax1, ax2, ax3], ['v', 'w', 'v + w'])
plt.title('Vectors $\mathbf{v}$, $\mathbf{w}$, and $\mathbf{v+w}$')

plt.show()
