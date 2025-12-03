import sys


def invalid_id_filter(*, id_ranges: list[tuple[str, str]]):
    for id_range in id_ranges:
        s, e = id_range
        for i in range(s, e + 1):
            si = str(i)
            max_w = len(si) // 2
            for w in range(1, max_w + 1):
                q, r = divmod(len(si), w)
                if r != 0:
                    continue
                if all(
                    si[o * w : (o + 1) * w] == si[(o + 1) * w : (o + 2) * w]
                    for o in range(q - 1)
                ):
                    yield i


print(
    sum(
        set(
            invalid_id_filter(
                id_ranges=[
                    tuple(map(int, r.strip().split("-")))
                    for r in sys.stdin.read().strip().split(",")
                ]
            )
        )
    )
)
