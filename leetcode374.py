n = 1
pick = 1
high = n
low = 0
while low <= high:
    mid = low + (high - low) // 2
    if mid == pick:
        print(mid)
        break
    elif mid < pick:
        low = mid + 1
    else:
        high = mid - 1
