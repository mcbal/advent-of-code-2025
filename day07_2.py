import sys
from functools import cache


def qbeam_propagation_timelines(qmanifold: list[list[str]]):
    instructions = qmanifold[::2]

    @cache
    def _paths_from(level, pos):
        if level + 1 == len(instructions):
            return 1
        if instructions[level + 1][pos] == "^":
            return _paths_from(level + 1, pos - 1) + _paths_from(level + 1, pos + 1)
        else:
            return _paths_from(level + 1, pos)

    return _paths_from(0, instructions[0].index("S"))


print(qbeam_propagation_timelines([list(ln.strip()) for ln in sys.stdin.readlines()]))
