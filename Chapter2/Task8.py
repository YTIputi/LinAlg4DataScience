import numpy as np
import matplotlib.pyplot as plt


a = np.array([[0.5], [2]])
b = np.array([[2], [1]])
beta = (a.T @ b) / (a.T @ a)
c = b - beta * a


plt.arrow(0, 0, a[0, 0], a[1, 0], head_width=.06, width=.01, color="k", length_includes_head=True, label="a")
plt.arrow(0, 0, b[0, 0], b[1, 0], head_width=.06, width=.01, color=[.8, .8, .8], length_includes_head=True, label="a")
plt.arrow((beta * a)[0, 0], (beta * a)[1, 0], c[0, 0], c[1, 0], head_width=.06, width=.01, color=[.5, .5, .5], length_includes_head=True, linestyle='--', label="b - beta * a")
plt.axis("square") 
plt.axis([0, 2.5, 0, 2.5])
plt.legend()
plt.show()

