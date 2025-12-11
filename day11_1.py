import sys
from functools import cache


def parse(lines: list[str]) -> dict[tuple[str]]:
    mapping = {}
    for ln in lines:
        k, *v = ln.split()
        mapping.update({k[:-1]: tuple(v)})
    return mapping


def you_to_out_paths(mapping: dict[tuple[str]]):

    @cache
    def _paths_from(label: str):
        if label == "out":
            return 1
        return sum(_paths_from(next_label) for next_label in mapping[label])

    return _paths_from("you")


print(you_to_out_paths(parse(sys.stdin.readlines())))
