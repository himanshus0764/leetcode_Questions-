nums = [2, 5, 1, 3, 4, 7]
n = 3
nums1 = []
for i in range(n):
    nums1.append(nums[i])
    nums1.append(nums[i + n])
print(nums1)