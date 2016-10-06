import heapq

a = [[1, 10, 34], [2, 5, 6], [10, 100, 101]]
heaparray = []
for i, l in enumerate(a):
    heaparray.append((l[0], 0, i))

heapq.heapify(heaparray)
max_seen = max(heaparray)[0]
diff_array = []
min_value = 100000000
while heaparray:
    val = heapq.heappop(heaparray)
    min_value = max_seen - val[0]
    diff_array.append((min_value, max_seen, val[0]))
    list_ind = val[2]
    index = val[1] + 1

    if index < len(a[list_ind]):
        max_seen = max(max_seen, a[list_ind][index])
        heapq.heappush(heaparray, (a[list_ind][index], index, list_ind))
    else:
        break

print "Range: ", diff_array[len(diff_array) - 1][2], diff_array[len(diff_array) - 1][1]
