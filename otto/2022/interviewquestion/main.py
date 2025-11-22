#!/usr/bin/env python3

import sys

startn = 0
a = 1  # fizz
b = 1  # buzz

a_n = []
b_n = []

l = []


def take_input():
    input()
    startn = int(input().split()[0])
    l = input().split()


def main():
    take_input()

    global startn
    num = startn

    for i in l:
        if i == "Fizz":
            a_n.append(num)
        if i == "Buzz":
            b_n.append(num)
        elif i == "FizzBuzz":
            a_n.append(num)
            b_n.append(num)

        startn += 1

    for i in range(sys.maxsize):
        is_prime = True
        for j in range(i):
            if i % j != 0:
                is_prime = False
                break

        if not is_prime:
            break


if __name__ == "__main__":
    main()
