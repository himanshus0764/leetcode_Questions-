class Solution(object):
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        nums_set = set(nums)
        n = 1
        while n in nums_set:
            n += 1

        return n