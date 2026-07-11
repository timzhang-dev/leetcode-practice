class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for index, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                temp = stack.pop()
                result[temp] = index - temp
            stack.append(index)
        return result