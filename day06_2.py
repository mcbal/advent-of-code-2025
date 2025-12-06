import sys
from functools import reduce
import numpy as np


def parse(sheet: list[list[str]]):
    ops = sheet[-1].split()
    chars = np.array([list(ln) for ln in sheet[:-1]], dtype="|S1")
    num_problems, num_chars = len(ops), chars.shape[-1]
    col = num_chars - 1
    for i in range(num_problems - 1, -1, -1):
        problem: list[int] = []
        while col >= 0 and not np.all(chars[:, col] == b" "):
            problem.append(int(chars[:, col].tobytes().strip().decode("utf-8")))
            col -= 1
        yield problem, ops[i]
        col -= 1  # jump to next problem


def homework(sheet: list[list[str]]):
    for args, op in parse(sheet):
        yield reduce(lambda x, y: x * y if op == "*" else x + y, map(int, args))


print(sum(homework([ln.strip("\n") for ln in sys.stdin.readlines()])))
