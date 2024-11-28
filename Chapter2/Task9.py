import numpy as np
import matplotlib.pyplot as plt

t = np.random.random((2, 1))
r = np.random.random((2, 1))
teta = (r.T @ t) / (r.T @ r)
a = teta * r
b = t - a

plt.arrow(0, 0, t[0, 0], t[1, 0], width=.01, color="k", length_includes_head=True, label="t")
plt.arrow(0, 0, r[0, 0], r[1, 0], width=.01, color=[.5, .5, .5], length_includes_head=True, label="r")
plt.arrow(0, 0, a[0, 0], a[1, 0], width=.01, color="k", length_includes_head=True, label="a", linestyle=':')
plt.arrow(0, 0, b[0, 0], b[1, 0], width=.01, color="k", length_includes_head=True, label="b", linestyle='--')

plt.axis('square')
plt.axis([-1, 1, -1, 1])
plt.legend()
plt.show()