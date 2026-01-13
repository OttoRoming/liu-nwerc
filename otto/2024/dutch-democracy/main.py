def init():
    """Read party data from input."""
    parties = []
    input()  # Read party count but don't store it
    for party_value in input().split(" "):
        parties.append(int(party_value))
    parties.sort()
    return parties


def search(party_index, parties, stack):
    """Search for party combinations."""
    stack.append(party_index)

    seats = 0
    for p in stack:
        seats += parties[p]

    print(stack)
    print(list(range(stack[-1] + 1, len(parties))))
    for i in range(stack[-1], len(parties)):
        print(i)
        search(i, parties, stack.copy())


def main():
    """Main entry point."""
    parties = init()
    for party_index in range(len(parties)):
        stack = []
        search(party_index, parties, stack)


if __name__ == "__main__":
    main()
