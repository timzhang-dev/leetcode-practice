class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char in "+*-/":
                a = stack.pop()
                b = stack.pop()
                if char == "+":
                    stack.append(a + b)
                if char == "*":
                    stack.append(a * b)
                if char == "-":
                    stack.append(b - a)
                if char == "/":
                    stack.append(int(b / a))

            else:
                stack.append(int(char))
        return stack[-1]
            