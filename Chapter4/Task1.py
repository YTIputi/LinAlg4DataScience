import numpy as np
import matplotlib.pyplot as plt


def corr(x: np.ndarray, y: np.ndarray) -> tuple[int, int]:
    xd, yd = x - x.mean(), y - y.mean()
    return (xd.T @ yd)[0, 0] / np.linalg.norm(xd) / np.linalg.norm(yd), (x.T @ y)[0, 0] / np.linalg.norm(x) / np.linalg.norm(y)

def corr2(x: np.ndarray, y: np.ndarray) -> tuple[int, int]:
    xd, yd = x - x.mean(), y - y.mean()
    return np.dot(xd, yd) / np.linalg.norm(xd) / np.linalg.norm(yd), np.dot(x, y) / np.linalg.norm(x) / np.linalg.norm(y)


# a = np.array([[0], [1], [2], [3]])
# b = np.array([[100], [101], [102], [103]])

# # plt.arrow(0, 0, a[0, 0], a[1, 0], color='r')
# # plt.arrow(0, 0, b[0, 0], b[1, 0], color=[.5, .5, .5])

# plt.axis('square')
# plt.savefig("test.png")

# print(corr(a, b))
