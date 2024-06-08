nums=[1,1,1,1]
goodpair=0
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            goodpair+=1
print(goodpair)