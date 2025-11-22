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
    a_n = []
    b_n = []
    num = startn

    for i in l:
        if i == "Fizz":
            a_n.append(num)
        if i == "Buzz":
            b_n.append(num)
        elif i == "FizzBuzz":
            a_n.append(num)
            b_n.append(num)

        num += 1

    return a_n, b_n


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
    _, _ = process_fizzbuzz(startn, l)
    find_prime_like()


if __name__ == "__main__":
    main()
