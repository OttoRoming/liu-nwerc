n = int(input())
groups = {}

total_count = 0

for _ in range(n):
    i, j, k = input().split()
    k = int(k)
    if i not in groups:
        groups[i] = {}
    groups[i][j] = k
    total_count += k

count = 0

for name, amounts in groups.items():
    left = amounts.get("left", 0)
    right = amounts.get("right", 0)
    m = max(left, right)

    if m == 0:
        if "any" in amounts:
            count += 1
    else:
        count += m

if total_count == count:
    print("impossible")
else:
    print(count + 1)
