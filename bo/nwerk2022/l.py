def expected(n, shirt_index, cycles):
    if cycles == 0:
        return shirt_index

    washed_index = (1 + (shirt_index + n) / 2) / 2
    unwashed_index = shirt_index

    wash_p = 1 - (shirt_index - 1) / n
    next_index = washed_index * wash_p + unwashed_index * (1 - wash_p)

    print(
        f"{shirt_index=}, {cycles=}, {washed_index=}, {unwashed_index=}, {wash_p=}, {next_index=}"
    )

    return expected(n, next_index, cycles - 1)


n, shirt_index, cycles = map(int, input().split())


probs = [0] * n
probs[shirt_index - 1] = 1

for i in range(cycles):
    next_probs = probs.copy()

    for j in range(probs):
        prob = probs[j]
        if prob == 0:
            continue

    probs = next_probs
