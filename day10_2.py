import sys
import numpy as np
from scipy.optimize import linprog


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
    for machine in machines:
        buttons, joltages = machine["buttons"], machine["joltages"]

        # integer linear programming min_x (c^T*x) with equality constraints A*x=b
        b_eq = np.asarray(joltages, dtype=np.int64)

        def _button_reprs():
            for i in range(len(buttons)):
                a = np.zeros_like(b_eq)
                for idx in buttons[i]:
                    a[idx] = 1
                yield a

        A_eq = np.stack([br for br in _button_reprs()]).T
        c = np.ones_like(A_eq[0, :])

        yield round(
            linprog(
                c,
                A_eq=A_eq,
                b_eq=b_eq,
                bounds=(0, np.inf),  # non-negative
                method="highs",
                integrality=1,  # enforce ints (some float solutions snap to lower-loss fractional presses)
            ).x.sum()
        )


print(f"\033[K{sum(fewest_button_presses(parse(sys.stdin.readlines())))}")
