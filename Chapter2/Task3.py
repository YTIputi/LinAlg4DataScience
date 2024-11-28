import numpy as np

def unit(x: np.ndarray) -> np.ndarray:
    return x / np.linalg.norm(x)


x = np.array([[2, 0, 0]])
z = np.array([[0], [0], [0]])
print(np.linalg.norm(unit(x)))