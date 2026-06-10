class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        maximum_left = 0
        maximum_right = 0
        total = 0
        while left < right:
            if height[left] <= height[right]:
                maximum_left = max(maximum_left, height[left])
                if maximum_left - height[left] > 0:
                    total += maximum_left - height[left]
                left += 1
            else:
                maximum_right = max(maximum_right, height[right])
                if maximum_right - height[right] > 0:
                    total += maximum_right - height[right]
                right -= 1
        return total