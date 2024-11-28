import numpy as np

def isCommut(x: np.ndarray, y: np.ndarray) -> bool:
    return (x.T @ y == y.T @ x)[0, 0]


print(isCommut(np.array([[1], [2]]), np.array([[2], [1]])))