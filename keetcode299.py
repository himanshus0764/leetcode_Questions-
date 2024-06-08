nums = [1,1,2,3]
nums2 = [0,1,1,1]
index = ""
bulls = 0
cows = 0

for i in range(len(nums)):
    if nums[i] == nums2[i]:
        bulls += 1
        index += str(i)
    elif nums[i] in nums2 and str(i) not in index:
        cows += 1
print(bulls,"B",cows,"A")