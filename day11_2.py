import sys
from functools import cache


def parse(lines: list[str]) -> dict[tuple[str]]:
    mapping = {}
    for ln in lines:
        k, *v = ln.split()
        mapping.update({k[:-1]: tuple(v)})
    return mapping


def svr_to_out_paths(mapping: dict[tuple[str]]):

    @cache
    def _paths_from(label: str, counter: int):
        if label == "out":
            return 1 if counter >= 2 else 0
        if label in ("dac", "fft"):
            # nodes only get visited once so counter maxes out at 2 (no cycles)?
            counter += 1
        return sum(_paths_from(next_label, counter) for next_label in mapping[label])

    return _paths_from("svr", 0)


print(svr_to_out_paths(parse(sys.stdin.readlines())))
