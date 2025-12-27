import itertools

matrix = []
for i in range(7):
    text = input()
    matrix.append([])
    for char in text:
        matrix[i].append(False if char == "x" else True)

d, h = map(int, input().split())

best = 0
for days in itertools.combinations(range(0, 7), d):
    hour_open_counts = []
    for hour in range(24):
        open_count = 0
        for day in days:
            if matrix[day][hour]:
                open_count += 1
        hour_open_counts.append(open_count)

    hour_open_counts.sort(reverse=True)
    count = sum(hour_open_counts[:h])
    best = max(best, count)

print(best / (d * h))
