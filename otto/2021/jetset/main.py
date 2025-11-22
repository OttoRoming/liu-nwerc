#!/usr/bin/env python3


def distance(start, end):
    """Calculate distance between two coordinates."""
    pos = start - end
    pos %= 360

    neg = end - start
    neg %= 360

    if pos > neg:
        return "neg", neg
    else:
        return "pos", pos


def read_coords():
    """Read coordinates from input."""
    coord_count = int(input())
    coords = []
    for i in range(coord_count):
        coords.append(int(input().split()[1]) + 180)
    return coords


def create_unvisited_set():
    """Create set of all possible longitude values."""
    unvisited = set()
    for i in range(360 * 2):
        lon = (i) / 2
        unvisited.add(lon)
    return unvisited


def process_coords(coords, unvisited):
    """Process coordinates and mark visited longitudes."""
    for i, coord in enumerate(coords):
        next_coord = coords[0] if i == len(coords) - 1 else coords[i + 1]

        dir, d = distance(coord, next_coord)
        
        if dir == "pos":
            r = range(coord * 2, (coord - d) * 2 - 1, -1)
        else:
            r = range(coord * 2, (coord + d) * 2 + 1)

        for step in r:
            i = (float(step) / 2) % 360
            print(coord, next_coord, dir, i)

            try:
                unvisited.remove(i)
            except KeyError:
                pass


def main():
    """Main entry point."""
    coords = read_coords()
    unvisited = create_unvisited_set()
    process_coords(coords, unvisited)

    if len(unvisited) == 0:
        print("yes")
    else:
        print("no", list(unvisited)[0] - 180.0)


if __name__ == "__main__":
    main()
