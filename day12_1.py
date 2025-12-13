import sys
import numpy as np


def parse(buffer):
    shapes, regions = [], []
    i = 0
    while i < len(buffer):
        if b":" in buffer[i] and b"x" not in buffer[i]:
            shapes.append(
                [
                    np.frombuffer(buffer[_i].strip(), dtype="|S1")
                    for _i in range(i + 1, i + 4)
                ]
            )
            i += 3
        elif b"x" in buffer[i]:
            region, shape_indices = buffer[i].split(b":")
            regions.append(
                (
                    tuple(map(int, region.split(b"x"))),
                    tuple(map(int, shape_indices.split())),
                )
            )
        i += 1
    return (np.asarray(shapes) == b"#").astype(np.bool_), regions


def valid_regions(
    shapes: np.ndarray, regions: list[tuple[tuple[int, int], np.ndarray]]
):
    # joke problem
    for region, shape_indices in regions:
        sum_of_shapes = sum(n * shapes[i].sum() for i, n in enumerate(shape_indices))
        yield sum_of_shapes <= region[0] * region[1]


print(sum(valid_regions(*parse(sys.stdin.buffer.readlines()))))
