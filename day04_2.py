import sys
import numpy as np


def valid_forklift_pos_mask(*, grid: np.ndarray, limit: int):
    padded_grid = np.pad(grid, (1, 1), "constant", constant_values=(b".", b"."))
    weights = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.uint8)
    windows = np.lib.stride_tricks.sliding_window_view(
        (padded_grid == b"@").astype(np.uint8), weights.shape
    )
    return (grid == b"@") * (np.einsum("ij,hwij->hw", weights, windows) < limit)


def remove(*, grid: np.ndarray, limit: int):
    removed_rolls = np.inf
    while removed_rolls > 0:
        removal_mask = valid_forklift_pos_mask(grid=grid, limit=limit)
        grid[removal_mask] = b"."
        removed_rolls = removal_mask.sum()
        yield removed_rolls


print(
    sum(
        remove(
            grid=np.stack(
                [
                    np.frombuffer(ln.strip(), dtype="|S1")
                    for ln in sys.stdin.buffer.readlines()
                ]
            ),
            limit=4,
        )
    )
)
