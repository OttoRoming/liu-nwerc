#!/usr/bin/env python3

import math

cranes = []

def init() -> None:
    crane_count = int(input())
    for i in range(crane_count):
        s = input().split(" ")
        cranes.append([int(s[0]), int(s[1]), int(s[2]), i])



def distance(first, other):
    x = first[0] - other[0]
    y = first[1] - other[1]
    return int(math.sqrt(x**2 + y**2))

def main() -> None:
    init()
    cranes.sort(key=lambda e: e[2]);
    area = 0

    crane_positions = []

    for crane in reversed(cranes):
        d: int = crane[2]
        for other_crane in crane_positions:
            # print(distance([4, 6], other_crane))
            d = min(d, distance(crane, other_crane))

        crane[2] = d
        crane_positions.append(list(crane))

    cranes.sort(key=lambda e: e[3]);
    for crane in cranes:
        pass
        print(crane[2])

main()
