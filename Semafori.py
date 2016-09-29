a, b = [int(n) for n in raw_input().split()]
time = 0
dist = 0
for i in range(0, a):
    c, e, f = [int(n) for n in raw_input().split()]
    time += c - dist
    dist = c
    if time % (e + f) <= e:
        time += e - (time % (e + f));
print time + b - c
