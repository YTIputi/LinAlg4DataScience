import numpy as np


def norm(x: np.ndarray) -> int:
    return np.sqrt(np.sum(x ** 2))


a = np.array([[1, 2, 3]])
b = np.array([[1], [3], [2]])

print(norm(a), norm(b))
