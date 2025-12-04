import sys
import numpy as np


def valid_forklift_pos_mask(*, grid: np.ndarray, limit: int):
    h, w = grid.shape
    padded_grid = np.pad(grid, (1, 1), "constant", constant_values=(b".", b"."))
    assert padded_grid.shape == (h + 2, w + 2)
    weights = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.uint8)
    windows = np.lib.stride_tricks.sliding_window_view(
        (padded_grid == b"@").astype(np.uint8), weights.shape
    )
    assert windows.shape == (h, w, 3, 3)
    return (grid == b"@") * (np.einsum("ij,hwij->hw", weights, windows) < limit)


print(
    valid_forklift_pos_mask(
        grid=np.stack(
            [
                np.frombuffer(ln.strip(), dtype="|S1")
                for ln in sys.stdin.buffer.readlines()
            ]
        ),
        limit=4,
    ).sum()
)
