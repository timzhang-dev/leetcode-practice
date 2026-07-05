class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        prefix_maximum = 0
        for i in range(n):
            prefix_maximum = max(prefix_maximum, height[i])
            prefix[i] = prefix_maximum
        
        suffix = [0] * n
        suffix_maximum = 0
        for i in range(n-1,-1,-1):
            suffix_maximum = max(suffix_maximum, height[i])
            suffix[i] = suffix_maximum

        total = 0
        for i in range(n):
            area = min(prefix[i],suffix[i]) - height[i] 
            total += area
        return total
        