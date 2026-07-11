class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char in "+-*/":
                first = stack.pop()
                second = stack.pop()
                if char == "+":
                    stack.append(int(first) + int(second))
                elif char == "-":
                    stack.append(int(second) - int(first))
                elif char == "*":
                    stack.append(int(first) * int(second))
                elif char == "/":
                    stack.append(int(second) / int(first))
            else:
                stack.append(char)
        return int(stack[-1])
            