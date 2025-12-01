import sys


def click(*, dial, moves):
    for move in map(list, moves):
        direction, amount = move[0], int("".join(move[1:]))
        dial = (
            (dial + amount) % 100 if direction == "R" else (100 - (amount - dial)) % 100
        )
        if dial == 0:
            yield True


print(sum(click(dial=50, moves=sys.stdin.read().splitlines())))
