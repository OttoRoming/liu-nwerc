#!/usr/bin/env python3


def shuffle_word(word):
    new_word = ""
    for i in range(len(word)):
        c = (i * 2) % len(word)
        new_word += word[c]
    return new_word


def main():
    i = int(input().split(" ")[-1])
    original_word = input()

    word = original_word
    iterations = 0

    while i > 0:
        word = shuffle_word(word)
        if word == original_word:
            i %= iterations
        iterations += 1
        i -= 1

    print(word)


main()
