level_n, queries = input("").split(" ")
level_n, queries = int(level_n), int(queries)

capacities = [int(cap) for cap in input("").split(" ")]
amounts = [0] * level_n

# key = level index
# value = next level index with bigger capacity
# -1 => no level with bigger capacity
next_larger = [-1] * level_n
stack = []
for i in range(level_n - 1, -1, -1):
    while stack and capacities[stack[-1]] <= capacities[i]:
        stack.pop()
    if stack:
        next_larger[i] = stack[-1]
    stack.append(i)

for i in range(queries):
    line = input("").split(" ")
    if line[0] == "+":
        level_index, amount = int(line[1]), int(line[2])
        level_index -= 1

        while level_index > -1:
            level_amount = amounts[level_index]
            level_cap = capacities[level_index]

            poured = min(amount, level_cap - level_amount)
            amounts[level_index] = level_amount + poured

            amount -= poured

            if amount <= 0:
                break

            level_index = next_larger[level_index]
    else:
        level = int(line[1])
        print(amounts[level - 1])
