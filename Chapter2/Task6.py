import numpy as np

def norm(x: np.ndarray) -> int:
    return ((x.T @ x) ** 0.5)[0, 0]


print(norm(np.array([[3], [4]])))