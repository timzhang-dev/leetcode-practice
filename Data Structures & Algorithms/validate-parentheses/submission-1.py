class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {")":"(", "]":"[", "}":"{"}
        stack = []
        for c in s:
            if stack and c in dictionary and stack[-1] == dictionary[c]:
                stack.pop()
            else:
                stack.append(c)
        return not stack
            