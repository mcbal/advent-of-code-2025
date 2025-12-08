import sys
import numpy as np


def dist(coords: np.ndarray):
    n = coords.shape[0]
    out = np.empty(int(n * (n - 1) / 2))
    unravel_idx_map = {}
    k = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            out[k] = np.linalg.norm(coords[i, :] - coords[j, :])
            unravel_idx_map[k] = (i, j)
            k += 1
    return out, unravel_idx_map


def jbox_circuits(*, coords: np.ndarray):
    n = coords.shape[0]
    dists, unravel_idx_map = dist(coords)
    sdists_idx = np.argsort(dists)
    circuits = {}
    p, c = 0, 0
    while len(circuits) < n or len(set(list(circuits.values()))) != 1:
        next_pair = sdists_idx[p]
        i, j = unravel_idx_map[next_pair]
        if i not in circuits and j not in circuits:
            # add i and j to new cluster
            circuits[i], circuits[j] = c, c
            c += 1
        elif i not in circuits and j in circuits:
            # add i to cluster j
            circuits[i] = circuits[j]
        elif i in circuits and j not in circuits:
            # add j to cluster i
            circuits[j] = circuits[i]
        else:
            if circuits[i] != circuits[j]:
                # merge cluster j into i
                js = [k for k, v in circuits.items() if v == circuits[j]]
                for j in js:
                    circuits[j] = circuits[i]
        p += 1
    return coords[i, 0] * coords[j, 0]


print(
    jbox_circuits(
        coords=np.asarray([list(map(int, c.split(","))) for c in sys.stdin.readlines()])
    )
)
