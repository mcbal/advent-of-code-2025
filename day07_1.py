import sys


def beam_propagation_splits(manifold: list[list[str]]):
    instructions = manifold[::2]
    num_levels, num_sites = len(instructions), len(instructions[0])

    state: list[bool] = [False] * num_sites
    state[instructions[0].index("S")] = True

    for level in range(1, num_levels):
        splits = 0
        for i in range(num_sites):
            if state[i] and instructions[level][i] == "^":
                state[i - 1], state[i], state[i + 1] = True, False, True
                splits += 1
        yield splits


print(
    sum(
        beam_propagation_splits([list(ln.strip()) for ln in sys.stdin.readlines()]),
    )
)
