#!/usr/bin/env python3

import sys


def take_input():
    """Read input data."""
    input()
    startn = int(input().split()[0])
    l = input().split()
    return startn, l


def process_fizzbuzz(startn, l):
    """Process fizzbuzz sequence."""
    num = startn

    for i in l:
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
    startn, l = take_input()
    process_fizzbuzz(startn, l)
    find_prime_like()


if __name__ == "__main__":
    main()
