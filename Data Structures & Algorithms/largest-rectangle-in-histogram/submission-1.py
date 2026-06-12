class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        maximum = 0
        for i in range(n):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                total = height * (i - index)
                maximum = max(maximum, total)
                start = index
            stack.append((start, heights[i]))
        
        for index, height in stack:
            total = height * (n - index)
            maximum = max(maximum, total)

        return maximum