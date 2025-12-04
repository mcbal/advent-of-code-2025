import sys


def jolts(*, banks: list[list[str]], n: int):
    for bank in banks:
        print("".join(["-"] * 80))

        m = len(bank)
        assert n <= m

        # init solution with first element in bank and bank tail
        solution: list[int] = [0] + list(range(m - n + 1, m))

        # cost function
        def _metric(_solution: list[int]) -> int:
            return int("".join(bank[i] for i in _solution))

        # try improving init solution by moving solution pointers
        s, b = 0, solution[0]  # solution pointer, bank pointer
        largest_joltage = _metric(solution)

        print(bank[b], solution, largest_joltage)

        while s < n:
            # lookahead
            if s + 1 == n:
                # this is last digit slot so window is region between current bank pointer and bank length
                window = m - b
            else:
                # until we hit next digit slot in solution
                window = solution[s + 1] - b

            # evaluate options
            scores = {}
            for w in range(window):
                solution[s] = b + w
                scores[w] = _metric(solution)

            # pick max score (or first one if tied / equal)
            w = max(scores, key=scores.get)
            largest_joltage = scores[w]  # monotonically increasing
            solution[s] = b + w

            # advance solution and bank pointers
            s += 1
            b += w + 1

            print(s, b, window, solution, _metric(solution))

        yield largest_joltage


print(
    sum(
        jolts(
            banks=[list(r.strip()) for r in sys.stdin.readlines()],
            n=12,
        )
    )
)  # also used n=2 (part 1) for debugging
