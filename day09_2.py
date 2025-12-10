#            _____
#         __|     |__
#      __|           |_
#    _|                |__
#  _|                     |_
# |___________________     _|
#  ___________________|   |_
# |_                       _|
#   |_                   _|
#     |_               _|
#       |__          _|
#          |________|


import sys
import numpy as np


def largest_constrained_rectangle_area(coords: np.ndarray) -> int:
    n = coords.shape[0]

    def _validate_rectangle_perimeter(
        _i: int, _j: int, _lava: np.ndarray
    ) -> tuple[bool, np.ndarray]:
        xmin, xmax = (
            min(coords[_i, 0], coords[_j, 0]),
            max(coords[_i, 0], coords[_j, 0]),
        )
        ymin, ymax = (
            min(coords[_i, 1], coords[_j, 1]),
            max(coords[_i, 1], coords[_j, 1]),
        )

        # early exit if rectangle contains known invalid points
        if np.any(
            (xmin <= _lava[:, 0])
            & (_lava[:, 0] <= xmax)
            & (ymin <= _lava[:, 1])
            & (_lava[:, 1] <= ymax)
        ):
            return False, _lava

        # build and validate perimeter (we only check perimeter)
        perimeter = []
        xrange, yrange = xmax + 1 - xmin, ymax + 1 - ymin
        for dx, dy in zip(range(xrange), range(yrange)):
            perimeter.extend(
                [
                    (xmin, ymin + dy),
                    (xmax, ymin + dy),
                    (xmin + dx, ymax),
                    (xmin + dx, ymin),
                ]
            )
        perimeter = np.unique(np.asarray(perimeter), axis=0)  # lazy deduplication

        # even/odd ray tracing: start outside (False)
        inside = np.zeros_like(perimeter[:, 0], dtype=np.bool_)
        for i in range(n):
            x1, y1, x2, y2 = (
                coords[i - 1][0],
                coords[i - 1][1],
                coords[i][0],
                coords[i][1],
            )
            mask = (
                (min(y1, y2) <= perimeter[:, 1])
                & (perimeter[:, 1] <= max(y1, y2))
                & (perimeter[:, 0] < max(x1, x2))
            )
            inside[mask] = ~inside[mask]

        # all perimeter points should be valid
        is_valid = np.all(inside)

        # extend lava with invalid points
        if not is_valid:
            _lava = np.unique(
                np.concatenate([_lava, perimeter[~inside]], axis=0), axis=0
            )

        return is_valid, _lava

    max_area, it, lava = 0, 0, np.empty((0, 2))
    for i in range(n - 1):
        for j in range(i + 1, n):
            is_valid, lava = _validate_rectangle_perimeter(i, j, lava)
            if is_valid:
                area = (
                    max(coords[i, 0], coords[j, 0])
                    + 1
                    - min(coords[i, 0], coords[j, 0])
                ) * (
                    max(coords[i, 1], coords[j, 1])
                    + 1
                    - min(coords[i, 1], coords[j, 1])
                )
                if area >= max_area:
                    max_area = area
            it += 1
            print(f"{max_area} ({it} / {int(n * (n - 1) / 2)})", end="\r", flush=True)

    return max_area


print(
    f"\033[K{largest_constrained_rectangle_area(
        coords=np.asarray([list(map(int, c.split(","))) for c in sys.stdin.readlines()])
    )}"
)
