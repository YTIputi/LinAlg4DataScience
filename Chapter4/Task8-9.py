import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


def claster(x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    N = x.shape[0]
    i1, i2, i3 = np.random.randint(0, N, size=(1, 3))[0]
    c1, c2, c3 = x[i1, :], x[i2, :], x[i3, :]
    d = {0: [], 1: [], 2: []}
    y = np.zeros(N)
    for _ in range(100):
        for j in range(N):
            y[j] = np.argmin([dist(x[j, :], c1), dist(x[j, :], c2), dist(x[j, :], c3)])
            d[y[j]].append(x[j, :])
        c1, c2, c3 = np.mean(np.array(d[0]), axis=0), np.mean(np.array(d[1]), axis=0), np.mean(np.array(d[2]), axis=0)
        d = {0: [], 1: [], 2: []}
    return y, np.array([c1, c2, c3])


def claster_v2(x: np.ndarray, n: int) -> tuple[np.ndarray, np.ndarray]:
    N = x.shape[0]
    index = np.random.randint(0, N, size=(1, n))[0]
    centeres = [x[i, :] for i in index]
    d = {i: [] for i in range(n)}
    y = np.zeros(N)
    for _ in range(100):
        for j in range(N):
            y[j] = np.argmin([dist(x[j, :], c) for c in centeres])
            d[y[j]].append(x[j, :])
        centeres = [np.mean(np.array(d[i]), axis=0) for i in range(n)]
        d = {i: [] for i in range(n)}
    return y, np.array(centeres)

def dist(x: np.ndarray, y: np.ndarray) -> float:
    return ((x - y) ** 2).sum()

def metric_dist(y: np.ndarray, centeres: np.ndarray, x: np.ndarray) -> float:
    N, s = x.shape[0], 0
    for j in range(N):
        s += dist(x[j, :], centeres[int(y[j])])
    return s


# fig, axe = plt.subplots(1, 2, figsize=(10, 5))

# x, y = make_blobs(500, 2, random_state=0)
# axe[0].scatter(x[:, 0], x[:, 1], c=y)
# axe[0].set_title("Изначальные данные")

# y, centres = claster(x)
# axe[1].scatter(x[:, 0], x[:, 1], c=y)
# axe[1].scatter(centres[:, 0], centres[:, 1], c="r")
# axe[1].set_title("Пересчитанные данные")
# plt.show()



# fig, axe = plt.subplots(1, 2, figsize=(10, 5))

# x, y = make_blobs(500, 2, random_state=0)
# axe[0].scatter(x[:, 0], x[:, 1], c=y)
# axe[0].set_title("Изначальные данные")

# y, centres = claster_v2(x, 6)
# axe[1].scatter(x[:, 0], x[:, 1], c=y)
# axe[1].scatter(centres[:, 0], centres[:, 1], c="r")
# axe[1].set_title("Пересчитанные данные")
# plt.show()

x, y = make_blobs(500, 2, random_state=0)
N = 10
result = np.zeros(N)
for i in range(N):
    result[i] = metric_dist(*claster_v2(x, i + 1), x)

plt.plot(result, marker="*")
plt.show()