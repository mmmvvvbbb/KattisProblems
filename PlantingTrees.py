num = input('')
gnum = raw_input()
x = [int(i) for i in gnum.split()]
x.sort()
day = 1
m = 0
for y in reversed(x):
    if(m < y + day):
        m = y + day
    day += 1
print m + 1
