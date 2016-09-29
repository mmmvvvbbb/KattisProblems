import sys

import math

# STILL WIP (BEDTIME)

def dist(x1, y1, x2, y2, expected):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= expected


for input in sys.stdin:
    a = float(input.split()[0])
    b = int(input.split()[1])
    x = []
    y = []
    if a == 0:
        exit()
    for i in range(0, b):
        hive = raw_input()
        c, d = [float[n] for n in hive.split()]
        x.append(c , d , True)
        print x
print x

