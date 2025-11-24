#!/usr/bin/env python3

import math


def read_input():
    """Read input data."""
    words = input().split(" ")
    socket_count = int(words[1])
    
    w = []
    for word in input().split(" "):
        w.append((float(word) / 3))
    w.sort()
    
    return socket_count, w


def calculate_adapters(socket_count, w):
    """Calculate number of adapters needed."""
    if socket_count < 3:
        return socket_count

    avail_sockets = socket_count - 2
    i = 0
    while avail_sockets > 0 and i < len(w) - 2:
        if i < len(w) - 3 and avail_sockets > math.ceil(w[i] + w[i + 1]):
            avail_sockets -= math.ceil(w[i] + w[i + 1])
            i += 2
        else:
            avail_sockets -= math.ceil(w[i])
            i += 1

    return i + 2


def main():
    """Main entry point."""
    socket_count, w = read_input()
    result = calculate_adapters(socket_count, w)
    print(result)


if __name__ == "__main__":
    main()
