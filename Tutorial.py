import math

a, b, c = [int(i) for i in raw_input().split()]
if c == 1:
    d = math.factorial(b)
elif c == 2:
    d = 2 ** b
elif c == 3:
    d = b ** 4
elif c == 4:
    d = b ** 3
elif c == 5:
    d = b ** 2
elif c == 6:
    d = b * math.log(b, 2)
elif c == 7:
    d = b
if d <= a:
    print "AC"
else:
    print "TLE"
