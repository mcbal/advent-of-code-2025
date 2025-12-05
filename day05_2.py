import sys


def parse_database(database: list[str]):
    i, ranges = 0, []
    for i, ln in enumerate(database):
        if ln == "\n":
            break
        s, e = map(int, ln.strip().split("-"))
        ranges.append([s, e + 1])  # shift inclusive end coordinate
    ids = [int(ln.strip()) for ln in database[i + 1 :]]
    return ranges, ids


def count_all_fresh_ingredient_ids(ranges: list[list[int, int]]):
    # sort intervals according to start coordinate (like bed files)
    sranges = sorted(ranges, key=lambda r: r[0])
    # merge intervals
    merged_sranges = [sranges[0]]
    for i in range(1, len(sranges)):
        prev = merged_sranges[-1]
        current = sranges[i]
        if current[0] <= prev[1]:
            # extend end of previous range
            prev[1] = max(current[1], prev[1])
        else:
            # or append a new non-overlapping one
            merged_sranges.append(current)
    return sum(r[1] - r[0] for r in merged_sranges)


print(count_all_fresh_ingredient_ids(parse_database(sys.stdin.readlines())[0]))
