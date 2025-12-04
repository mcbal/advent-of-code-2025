import sys


def jolts(*, banks: list[list[int]]):
    for bank in banks:
        max_joltage = 0
        for i in range(len(bank) - 1):
            for j in range(len(bank) - 1, i, -1):
                if int(str(bank[i]) + str(bank[j])) > max_joltage:
                    max_joltage = int(str(bank[i]) + str(bank[j]))
        yield max_joltage


print(
    sum(jolts(banks=[list(map(int, list(ln.strip()))) for ln in sys.stdin.readlines()]))
)
