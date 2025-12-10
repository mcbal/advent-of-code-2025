import sys
import numpy as np


def areas(coords: np.ndarray):
    n = coords.shape[0]
    out = np.empty(int(n * (n - 1) / 2), dtype=coords.dtype)
    k = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            out[k] = (
                max(coords[i, 0], coords[j, 0]) + 1 - min(coords[i, 0], coords[j, 0])
            ) * (max(coords[i, 1], coords[j, 1]) + 1 - min(coords[i, 1], coords[j, 1]))
            k += 1
    return out


def largest_rectangle_area(*, coords: np.ndarray):
    return np.amax(areas(coords))


print(
    largest_rectangle_area(
        coords=np.asarray([list(map(int, c.split(","))) for c in sys.stdin.readlines()])
    )
)
