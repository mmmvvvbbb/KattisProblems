num = raw_input()
x = [int(i) for i in raw_input().split()]
x.sort(reverse=True)
print sum(x[2::3])
