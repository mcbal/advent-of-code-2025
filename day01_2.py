import sys


def click(*, dial, moves):
    for move in map(list, moves):
        direction, amount = move[0], int("".join(move[1:]))
        if direction == "R":
            num_hits, dial = (dial + amount) // 100, (dial + amount) % 100
        else:
            num_hits = amount // 100
            if dial > 0 and amount % 100 >= dial:
                num_hits += 1
            dial = (100 - (amount - dial)) % 100
        yield num_hits


print(sum(click(dial=50, moves=sys.stdin.read().splitlines())))
