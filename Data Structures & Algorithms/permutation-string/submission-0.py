from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = defaultdict(int)
        for char in s1:
            dict1[char] += 1
        
        n = len(s1)
        left = 0
        right = n - 1 

        m = len(s2)
        dict2 = defaultdict(int)
        for char in s2[:right + 1]:
            dict2[char] += 1
        if dict1 == dict2:
                return True
        while right < m - 1:
            right += 1
            dict2[s2[right]] += 1
            dict2[s2[left]] -= 1
            if dict2[s2[left]] == 0:
                del dict2[s2[left]]
            left += 1
            if dict1 == dict2:
                return True
        return False

