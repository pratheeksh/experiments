interval = sorted([(1, 2), (2, 5), (3, 5) , (8,9),(4, 6), (7, 8), (2, 3)])
ind = 1
res = []
cur = interval[0]
print interval
stack = [interval[0]]
while ind != len(interval):
    nex = interval[ind]

    if cur[1] >= nex[0]:
        stack.pop()
        new_int = (cur[0], max(cur[1], nex[1]))
        cur = new_int
    else:
        cur = nex
    stack.append(cur)
    print stack
    ind += 1
print stack
