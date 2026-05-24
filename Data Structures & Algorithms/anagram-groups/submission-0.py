from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for s in strs:
            array = [0] * 26
            for c in s:
                index = ord(c) - ord("a")
                array[index] += 1
            dictionary[tuple(array)].append(s)
        
        return list(dictionary.values())