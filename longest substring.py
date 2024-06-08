class Solution(object):
    @classmethod
    def lengthOfLongestSubstring(cls, s):
        start = maxi = 0
        char = {}
        for i, c in enumerate(s):
            start = max(start, char.get(c, -1) + 1)
            char[c] = i
            maxi = max(maxi, i - start + 1)
        return maxi

s = "abcabcbb"
print(Solution.lengthOfLongestSubstring(s))
