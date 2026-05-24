from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary1 = defaultdict(int)
        dictionary2 = defaultdict(int)
        for char in s:
            dictionary1[char] += 1
        for char in t:
            dictionary2[char] += 1
        
        return dictionary1 == dictionary2
        