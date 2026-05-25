class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {')':'(',']':'[','}':'{'}
        stack = []
        for char in s:
            if char in dictionary:
                if stack and stack[-1] == dictionary[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
            