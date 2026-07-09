class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {")":"(", "]":"[", "}":"{"}
        stack = []
        for c in s:
            if c in dictionary:
                if stack and stack[-1] == dictionary[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
            