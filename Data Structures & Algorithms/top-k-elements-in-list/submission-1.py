from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        array = [[] for _ in range(len(nums)+1)]
        for key, val in counts.items():
            array[val].append(key)
        result = []
        count = 0
        for i in range(len(array)-1,0,-1):
                for num in array[i]:
                    result.append(num)
                    if len(result) == k:
                        return result
        




