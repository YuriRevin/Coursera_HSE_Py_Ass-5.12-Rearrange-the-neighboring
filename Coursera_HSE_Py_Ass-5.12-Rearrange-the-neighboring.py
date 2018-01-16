l = list(map(int, input().split()))
if len(l) % 2 == 0:
    for i in range(0, len(l), 2):
        t = l[i]
        l[i] = l[i+1]
        l[i+1] = t
else:
    for i in range(0, len(l)-1, 2):
        t = l[i]
        l[i] = l[i+1]
        l[i + 1] = t

print(' '.join(map(str, l)))
