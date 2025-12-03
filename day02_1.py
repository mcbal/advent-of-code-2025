import sys


def invalid_id_filter(*, id_ranges: list[tuple[str, str]]):
    for id_range in id_ranges:
        s, e = id_range
        for i in range(s, e + 1):
            si = str(i)
            if len(si) % 2 != 0:
                continue
            max_w = len(si) // 2
            for w in range(1, max_w + 1):
                if si[:w] == si[w:]:
                    yield i


print(
    sum(
        invalid_id_filter(
            id_ranges=[
                tuple(map(int, r.strip().split("-")))
                for r in sys.stdin.read().strip().split(",")
            ]
        )
    )
)
