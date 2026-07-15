class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for index, height in enumerate(heights):
            start = index
            while stack and height < stack[-1][1]:
                i, val = stack.pop()
                width = index - i
                area = width * val
                max_area = max(max_area, area)
                start = i
            stack.append((start, height))
        
        for index, height in stack:
            width = len(heights) - index
            area = width * height
            max_area = max(max_area, area)
        
        return max_area