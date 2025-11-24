

def find_path(from_node, to_node, neighbors, n):
    dist = {from_node: 0}
    remaining = list(range(n))

    while remaining:
        node = remaining[0]
        for other_node in remaining:
            if dist.get(other_node, 999999) < dist.get(node, 999999):
                node = other_node
        node_dist = dist[node]

        for neighbor, cost in neighbors[node]:
            new_dist = node_dist + cost

            if neighbor in dist and dist[neighbor] < new_dist:
                # vi har en lägre kostnad
                new_dist = dist[neighbor]
            else:
                # ny lägre kostnad
                dist[neighbor] = new_dist

            if neighbor == to_node:
                return new_dist

        remaining.remove(node)


def main():
    n, m, k = map(int, input().split())
    # for each node, an array of (i, cost) where i is another node and cost the distance between them
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        i, j, cost = map(int, input().split())
        neighbors[i - 1].append((j - 1, cost))
        neighbors[j - 1].append((i - 1, cost))

    # list of tuples (p, cost)
    paths = []
    for _ in range(k):
        i, p = input().split()
        i = int(i)
        p = float(p)

        cost = find_path(0, i - 1, neighbors, n)
        cost += find_path(i - 1, n - 1, neighbors, n)
        paths.append((p, cost))

    total = 0
    prob_left = 1
    paths.sort(key=lambda tuple: tuple[1])

    for p, cost in paths:
        p *= prob_left
        prob_left -= p
        total += p * cost

    if prob_left > 0:
        print("impossible")
    else:
        print(total)


if __name__ == "__main__":
    main()
