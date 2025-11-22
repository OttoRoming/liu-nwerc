def init():
    """Read party data from input."""
    parties = []
    parties_count = int(input())
    for i in input().split(" "):
        parties.append(int(i))
    parties.sort()
    return parties


def search(party, parties, stack):
    """Search for party combinations."""
    stack.append(party)

    seats = 0
    for p in stack:
        seats += parties[p]

    print(stack)
    print(list(range(stack[-1] + 1, len(parties))))
    for i in range(stack[-1], len(parties)):
        print(i)
        search(i, parties, stack)


def main():
    """Main entry point."""
    parties = init()
    for party in parties:
        stack = []
        search(party, parties, stack)


if __name__ == "__main__":
    main()
