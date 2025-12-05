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


def is_fresh_ingredient_id(ranges: list[list[int, int]], ids: list[int]):
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
    # we now loop over sorted ids and sorted merged ranges to avoid doing too much work
    sids = sorted(ids)
    s_idx, r_idx, last_r_idx = 0, 0, 0
    while s_idx < len(sids):
        while r_idx < len(merged_sranges):
            if merged_sranges[r_idx][0] <= sids[s_idx] < merged_sranges[r_idx][1]:
                last_r_idx = r_idx
                yield True
                break
            r_idx += 1
        r_idx = last_r_idx  # set range pointer to last known hit (we can ignore smaller intervals for next id because ids are sorted)
        s_idx += 1  # move to next id to check


print(sum(is_fresh_ingredient_id(*parse_database(sys.stdin.readlines()))))
