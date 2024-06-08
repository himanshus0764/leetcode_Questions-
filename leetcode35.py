nums = [1, 3, 5, 6]
target = 7
maxindex = 0
for i in range(len(nums)):
    if nums[i] <= target:
        maxindex = i+1
print(maxindex)
