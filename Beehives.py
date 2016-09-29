import math


def dist(x1, y1, x2, y2, expected):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= expected


for useless in range(10):
    a, b = raw_input().split()
    a = float(a)
    b = int(b)
    if b == 0:
        break
    x = []
    y = []
    z = []
    for i in range(b):
        xt, yt = raw_input().split()
        z.append(True)
        for r, u in enumerate(x):
            if dist(float(xt), float(yt), u, y[r], a):
                z[i] = False
                z[r] = False
        x.append(float(xt))
        y.append(float(yt))

    print b - sum(z), "sour,", sum(z), "sweet"
