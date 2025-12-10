import sys
from collections import deque
from functools import cache


def parse(lines: list[str]):
    machines = []
    for ln in lines:
        lights, *buttons, joltages = ln.split()
        machines.append(
            {
                "lights": tuple(c == "#" for c in list(lights[1:-1])),
                "buttons": [tuple(map(int, b[1:-1].split(","))) for b in buttons],
                "joltages": list(map(int, joltages[1:-1].split(","))),
            }
        )
    return machines


def fewest_button_presses(machines: list[dict]):
    for machine_idx, machine in enumerate(machines):
        lights, buttons = machine["lights"], machine["buttons"]

        @cache
        def toggle(state: tuple[bool], button: tuple[int]):
            return tuple(not s if i in button else s for i, s in enumerate(state))

        # bfs
        state = tuple(False for _ in range(len(lights)))
        queue = deque()
        queue.extend((1, toggle(state, button), button) for button in buttons)
        while queue:
            i, state, button = queue.popleft()
            if state == lights:
                print(
                    f"Machine {machine_idx} / {len(machines)}: {i} presses",
                    end="\r",
                    flush=True,
                )
                yield i
                break  # bfs so we break at first hit to get min i cost
            queue.extend(
                (i + 1, toggle(state, next_button), next_button)
                for next_button in buttons
                if next_button != button
            )


print(f"\033[K{sum(fewest_button_presses(parse(sys.stdin.readlines())))}")
