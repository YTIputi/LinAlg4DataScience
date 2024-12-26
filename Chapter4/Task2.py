import numpy as np
import matplotlib.pyplot as plt
import Task1

x = np.arange(4)
offset = np.arange(-50, 50)
res = np.zeros((offset.shape[0], 2))


for i in range(offset.shape[0]):
    res[i, :] = Task1.corr2(x, x + offset[i])

plt.plot(offset, res[:, 0], color='black', marker='o', label="Пирсон")
plt.plot(offset, res[:, 1], color='grey', marker='*', label="Косинусное сход.")
plt.legend()
plt.savefig('test.png')