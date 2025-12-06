import sys
from functools import reduce


def homework(sheet: list[list[str]]):
    for *args, op in zip(*sheet[:-1], sheet[-1]):
        yield reduce(lambda x, y: x * y if op == "*" else x + y, map(int, args))


print(sum(homework([ln.split() for ln in sys.stdin.readlines()])))
