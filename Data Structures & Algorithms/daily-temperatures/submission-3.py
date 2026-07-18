class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n
        for index, value in enumerate(temperatures):
            while stack and value > temperatures[stack[-1]]:
                temp = stack.pop()
                result[temp] = index - temp
            stack.append(index)
        return result
