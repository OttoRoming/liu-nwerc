#!/usr/bin/env python3


def angle_between(n, a, b):
    # Normalize to 0–360
    n = n % 360
    a = a % 360
    b = b % 360

    # Forward distance from a to b
    d_ab = (b - a) % 360

    # If the forward path a→b is the short arc
    if d_ab <= 180:
        # Check if n lies on the arc a→b
        d_an = (n - a) % 360
        return 0 <= d_an <= d_ab
    else:
        # Otherwise the short arc is b→a (the other direction)
        # Check if n lies on that arc
        d_na = (a - n) % 360
        return 0 <= d_na <= (360 - d_ab)


coord_count = int(input())
coords = []
for i in range(coord_count):
    coords.append(int(input().split()[1]) + 180)

unvisited = []
for i in range(360 * 2):
    lon = i / 2
    unvisited.append(lon)


for i, coord in enumerate(coords):
    next: int
    if i == len(coords) - 1:
        next = coords[0]
    else:
        next = coords[i + 1]

    i = 0
    while i < len(unvisited):
        long = unvisited[i]

        if angle_between(long, coord, next):
            unvisited.pop(i)
        else:
            i += 1

if len(unvisited) == 0:
    print("yes")
else:
    print("no", unvisited[0] - 180.0)
