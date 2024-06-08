class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area, max_area = 0, 0
        l, r = 0, len(height) - 1
        while r > l:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return max_area