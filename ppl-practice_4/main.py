import numpy as np


def add(def_a, def_b):
    np_a, np_b = np.array(def_a), np.array(def_b)
    if np_a.shape == np_b.shape:
        flat_np_a, flat_np_b = np_a.flatten(), np_b.flatten()
        return np.array([flat_np_a[i] + flat_np_b[i] for i in range(len(flat_np_a))]).reshape(-1, np_a.shape[1])
    else:
        raise ValueError("Initial matrices must be the same shape.")


def transpose(def_a):
    np_a, np_c = np.array(def_a), np.array(def_a)
    for row in range(np_a.shape[0]):
        for col in range(np_a.shape[1]):
            np_c[col][row] = np_a[row][col]
    return np_c


if __name__ == "__main__":
    a, b = [[1, 2, 3], [4, 5, 6]], [[2, 3, 4], [5, 6, 7]]
    print(a, b)
    print(add(a, b))
    print(transpose(a))
