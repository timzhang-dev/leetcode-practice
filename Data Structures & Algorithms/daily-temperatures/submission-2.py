class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for index, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                temp = stack.pop()
                result[temp] = index - temp
            stack.append(index)
        return result