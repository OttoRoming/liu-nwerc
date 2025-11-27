#!/usr/bin/env python3

import math


def read_input():
    """Read input data."""
    words = input().split(" ")
    socket_count = int(words[1])
    
    widths = []
    for word in input().split(" "):
        widths.append((float(word) / 3))
    widths.sort()
    
    return socket_count, widths


def calculate_adapters(socket_count, widths):
    """Calculate number of adapters needed."""
    if socket_count < 3:
        return socket_count

    avail_sockets = socket_count - 2
    i = 0
    while avail_sockets > 0 and i < len(widths) - 2:
        if i < len(widths) - 3 and avail_sockets > math.ceil(widths[i] + widths[i + 1]):
            avail_sockets -= math.ceil(widths[i] + widths[i + 1])
            i += 2
        else:
            avail_sockets -= math.ceil(widths[i])
            i += 1

    return i + 2


def main():
    """Main entry point."""
    socket_count, widths = read_input()
    result = calculate_adapters(socket_count, widths)
    print(result)


if __name__ == "__main__":
    main()
