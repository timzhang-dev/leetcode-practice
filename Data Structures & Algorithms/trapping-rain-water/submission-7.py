class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        total = 0
        max_left = 0
        max_right = 0
        while left < right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            if max_left <= max_right:
                left += 1
                total += max(0, max_left - height[left])
            else:
                right -= 1
                total += max(0, max_right - height[right])
        return total