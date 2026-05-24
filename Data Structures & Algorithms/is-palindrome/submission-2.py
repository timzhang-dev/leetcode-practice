class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isLetter(c):
            if ord(c) >= ord("a") and ord(c) <= ord("z"):
                return True
            if ord(c) >= ord("A") and ord(c) <= ord("Z"):
                return True
            if ord(c) >= ord("0") and ord(c) <= ord("9"):
                return True
            return False

        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not isLetter(s[left]):
                left += 1
            while left < right and not isLetter(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

        

