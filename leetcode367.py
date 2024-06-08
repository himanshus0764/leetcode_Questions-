num = 14
high = num
low = 0
while True:
    mid = low = (high - low) // 2
    x = mid * mid
    if x == num:
        print("true")
        break
    elif num/2 > num:
        high = mid - 1
    else:
        low = mid + 1
if low>high:
    print("false")