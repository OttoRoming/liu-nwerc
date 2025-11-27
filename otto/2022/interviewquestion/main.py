#!/usr/bin/env python3

import sys


def take_input():
    """Read input data."""
    input()
    startn = int(input().split()[0])
    sequence = input().split()
    return startn, sequence


def process_fizzbuzz(startn, sequence):
    """
    Placeholder for processing a fizzbuzz sequence.
    Currently, this function increments the starting number for each element in the list,
    but does not use or return the results. Intended for future implementation.
    """
    num = startn

    for _ in sequence:
        # Process the fizzbuzz sequence (results not currently used)
        num += 1


def find_prime_like():
    """Find a prime-like number."""
    for i in range(sys.maxsize):
        is_prime = True
        for j in range(i):
            if i % j != 0:
                is_prime = False
                break

        if not is_prime:
            break


def main():
    """Main entry point."""
    startn, sequence = take_input()
    process_fizzbuzz(startn, sequence)
    find_prime_like()


if __name__ == "__main__":
    main()
