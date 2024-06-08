nums = [3,2,1,0,4]
lastpos = len(nums) - 1
b=0
for i in range(len(nums) - 2, -1, -1):
    if i + nums[i] >= lastpos:
        lastpos = i
        b=0
if b!=0:
    print("true")
else:
    print("false")
