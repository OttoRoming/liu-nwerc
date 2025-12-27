n = int(input())

output = []

for i in range(n):
    nums = map(int, input().split())
    for j, cost in enumerate(nums):
        if cost != -1:
            output.append((i, j, cost))

output.sort(key=lambda tuple: tuple[0] * n + tuple[1])

print(len(output))
for i, j, cost in output:
    print(i + 1, j + 1, cost)
