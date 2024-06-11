nums = [0, 1, 0, 3, 12]
result = []
for i in nums[:]:
    if i == 0:
        result.append(i)
        nums.remove(i)
print(nums + result)
