class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0
        while left < right:
            area = min(heights[right], heights[left])*(right - left)
            result = max(area, result)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return result