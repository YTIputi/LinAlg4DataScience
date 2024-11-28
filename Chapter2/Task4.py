import numpy as np

def module(v: np.ndarray, x: int) -> np.ndarray:
    return v * x / np.linalg.norm(v)


v = np.array([[1, 1]])
print(module(v, 2), np.linalg.norm(module(v, 2)))