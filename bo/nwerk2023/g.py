import math


n, m, q = map(int, input().split())
planet_coords = []
neighbor_map = []
for _ in range(n):
    x, y, z = map(int, input().split())
    planet_coords.append((x, y, z))
    neighbor_map.append([])

for _ in range(m):
    a, b = map(int, input().split())
    neighbor_map[a - 1].append(b - 1)
    neighbor_map[b - 1].append(a - 1)

missions = []
for _ in range(q):
    c, t = map(int, input().split())
    missions.append((c, t))


def dist(start, end):
    start_x, start_y, start_z = planet_coords[start]
    end_x, end_y, end_z = planet_coords[end]
    return math.sqrt(
        (start_x - end_x) ** 2 + (start_y - end_y) ** 2 + (start_z - end_z) ** 2
    )


def dijkstra(start, end):
    open_set = {start}
    came_from = {}

    g_score = {}
    g_score[start] = 0

    f_score = {}
    f_score[start] = dist(start, end)

    while open_set:
        lowest_f_score = 0
        current = None
        for planet in open_set:
            planet_f_score = f_score[planet]
            if current is None or planet_f_score < lowest_f_score:
                current = planet
                lowest_f_score = planet_f_score

        if current == end:
            path = [end]
            while True:
                next = came_from[current]
                if next == start:
                    break
                path.append(next)
                current = next
            path.reverse()
            return path, g_score[end]

        open_set.remove(planet)
        for neighbor in neighbor_map[current]:
            tentative_g_score = g_score[current] + dist(current, neighbor)
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + dist(neighbor, end)
                open_set.add(neighbor)

    return None


current_planet = 0

for target_planet, time_limit in missions:
    result = dijkstra(current_planet, target_planet - 1)
    if result is None:
        print("impossible (no path)")
        continue
    path, total_distance = result

    used_fuel = 0
    possible = True
    for next_planet in path:
        distance = dist(current_planet, next_planet)

        max_time = time_limit * (distance / total_distance)

        discriminant = max_time**2 / 4 - distance
        if discriminant < 0:
            print("impossible (reached time limit)")
            possible = False
            current_planet = target_planet - 1
            break

        t_a = max_time / 2 + math.sqrt(discriminant)
        used_fuel += 2 * t_a

        current_planet = next_planet

    if possible:
        print(used_fuel)
