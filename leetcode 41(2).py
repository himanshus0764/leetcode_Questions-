class Solution(object):
    def firstMissingPositive(self, nums):
        num_set = set(nums)
        a = 1
        while True:
            if a not in num_set:
                return a
            a += 1