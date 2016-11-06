arr = [1, 2, 1, 0, 2, 1, 1, 1, 2, 2, 1, 1, 1, 0]
start, mid = 0, 0
end = len(arr) - 1
while mid <= end:
    print start, mid, end, arr
    if arr[mid] == 0:
        arr[mid], arr[start] = arr[start], arr[mid]
        start += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    elif arr[mid] == 2:
        arr[mid], arr[end] = arr[end], arr[mid]
        end -= 1

print arr
