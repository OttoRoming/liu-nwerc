#!/usr/bin/env python3

def distance(start, end):
    pos = start - end
    pos %= 360

    neg = end - start
    neg %= 360

    if pos > neg:
        return "neg", neg
    else:
        return "pos", pos


coord_count = int(input())
coords = []
for i in range(coord_count):
    coords.append(int(input().split()[1])+180)

unvisited = set()
for i in range(360*2):
    lon = (i)/2
    unvisited.add(lon)


for i, coord in enumerate(coords):
    next: int
    if i == len(coords) - 1:
        next = coords[0]
    else:
        next = coords[i+1]


    dir, d = distance(coord, next)
    r: range
    if dir == "pos":
        r = range(coord*2, (coord-d)*2-1, -1)
    else:
        r = range(coord*2, (coord+d)*2+1)

    for step in r:
        i = (float(step)/2)%360
        print (coord, next, dir, i)

        try:
            unvisited.remove(i)
        except KeyError:
            pass

if len(unvisited) == 0:
    print("yes")
else:
    print("no", list(unvisited)[0]-180.0)
