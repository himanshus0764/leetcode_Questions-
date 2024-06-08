x = 4
low = 0
high = x
while low <= high:
    mid = low + (high - low) // 2
    if mid == x:
        print(mid)
    elif mid > x:
        low = mid + 1
    else:
        high = mid - 1
