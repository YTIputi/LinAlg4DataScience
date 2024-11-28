import numpy as np

def trans(x: np.ndarray) -> np.ndarray:
    y = np.zeros(x.shape[::-1])
    for i in range(x.shape[1]):
        y[i, 0] = x[0, i]
    return y

a = np.array([[1, 2, 3, 4, 5, 6, 7]])
print(trans(a))
