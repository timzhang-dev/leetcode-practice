class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        array1 = [0] * 26
        array2 = [0] * 26
        for i in range(n):
            array1[ord(s1[i]) - ord('a')] += 1
            array2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if array1[i] == array2[i]:
                matches += 1
        left = 0
        for i in range(n,m):
            if matches == 26:
                return True
            index = ord(s2[i]) - ord('a')
            array2[index] += 1
            if array1[index] == array2[index]:
                matches += 1
            elif array1[index] + 1 == array2[index]:
                matches -= 1
            
            index = ord(s2[left]) - ord('a')
            array2[index] -= 1
            if array1[index] == array2[index]:
                matches += 1
            elif array1[index] - 1 == array2[index]:
                matches -= 1
            left += 1
        return matches == 26


