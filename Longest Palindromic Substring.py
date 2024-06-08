class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        result =0
        for char in s:
            if char not in seen:
                result +=1
                seen.add(char)
            else:
                break
        return (result)
