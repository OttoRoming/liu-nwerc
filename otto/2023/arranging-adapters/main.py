#!/usr/bin/env python3

import math
import sys

charger_count = 0
socket_count = 0

words = input().split(" ")
charger_count = int(words[0])
socket_count = int(words[1])

if socket_count < 3:
    print(socket_count)
    sys.exit(0)

w = []
for word in input().split(" "):
    w.append((float(word) / 3))
w.sort()

avail_sockets = socket_count - 2
i = 0
while avail_sockets > 0 and i < len(w) - 2:
    if i < len(w) - 3 and avail_sockets > math.ceil(w[i] + w[i + 1]):
        avail_sockets -= math.ceil(w[i] + w[i + 1])
        i += 2
    else:
        avail_sockets -= math.ceil(w[i])
        i += 1


print(i + 2)
