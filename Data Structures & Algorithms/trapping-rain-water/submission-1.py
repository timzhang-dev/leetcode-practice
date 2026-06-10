class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = []
        maximum = 0
        for i in range(n):
            maximum = max(height[i], maximum)
            prefix.append(maximum)
        
        maximum = 0
        suffix = []
        for i in range(n-1,-1,-1):
            maximum = max(height[i], maximum)
            suffix.append(maximum)
        suffix.reverse()
        
        total = 0
        for i in range(n):
            water = min(prefix[i], suffix[i]) - height[i]
            if water > 0:
                total += water
        return total