#!/usr/bin/env python3

import math


def init():
    """Read crane data from input."""
    cranes = []
    crane_count = int(input())
    for idx in range(crane_count):
        s = input().split(" ")
        cranes.append([int(s[0]), int(s[1]), int(s[2]), idx])
    return cranes


def distance(first, other):
    """Calculate distance between two cranes."""
    x = first[0] - other[0]
    y = first[1] - other[1]
    return int(math.sqrt(x**2 + y**2))


def process_cranes(cranes):
    """Process cranes to calculate minimum distances."""
    cranes.sort(key=lambda e: e[2])
    crane_positions = []

    for crane in reversed(cranes):
        d = crane[2]
        for other_crane in crane_positions:
            d = min(d, distance(crane, other_crane))

        crane[2] = d
        crane_positions.append(list(crane))

    cranes.sort(key=lambda e: e[3])
    return cranes


def main():
    """Main entry point."""
    cranes = init()
    cranes = process_cranes(cranes)
    
    for crane in cranes:
        print(crane[2])


if __name__ == "__main__":
    main()
