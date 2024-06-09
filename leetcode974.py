nums = [4, 5, 0, -2, -3, 1]
k = 5

subarrays = 0
prefixSum = 0
remainderCount = {0: 1}

for num in nums:
    prefixSum += num
    remainder = prefixSum % k

    if remainder < 0:
        remainder += k

    if remainder in remainderCount:
        subarrays += remainderCount[remainder]
        remainderCount[remainder] += 1
    else:
        remainderCount[remainder] = 1

print(subarrays)
