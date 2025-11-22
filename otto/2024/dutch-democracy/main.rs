parties = []


def init() -> None:
    parties_count = int(input())
    for i in input().split(" "):
        parties.append(int(i))
    parties.sort()


stack = []


def search(party: int) -> None:
    stack.append(party)

    seats = 0
    for p in stack:
        seats += parties[p]

    print(stack)
    print(list(range(stack[-1] + 1, len(parties))))
    for i in range(stack[-1], len(parties)):
        print(i)
        search(party)


def main() -> None:
    init()
    for party in parties:
        search(party)


if __name__ == "__main__":
    main()
