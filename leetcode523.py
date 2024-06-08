nums = [0]
k = 1

if k == 0:
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0:
            print(True)
            break
    else:
        print(False)
else:
    remainderdict = {0: -1}
    cumulativesum = 0

    for i in range(len(nums)):
        cumulativesum += nums[i]
        remainder = cumulativesum % k

        if remainder in remainderdict:
            if i - remainderdict[remainder] > 1:
                print(True)
                break
        else:
            remainderdict[remainder] = i
    else:
        print(False)
