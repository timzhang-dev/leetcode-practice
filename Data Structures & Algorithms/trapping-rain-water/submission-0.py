class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = []
        for i in range(n):
            if i > 0:
                maximum = max(height[:i+1])
            else:
                maximum = 0
            prefix.append(maximum)
        
        suffix = []
        for i in range(n):
            if i < n - 1:
                maximum = max(height[i:])
            else:
                maximum = 0
            suffix.append(maximum)
        
        total = 0
        for i in range(n):
            water = min(prefix[i], suffix[i]) - height[i]
            if water > 0:
                total += water
        return total