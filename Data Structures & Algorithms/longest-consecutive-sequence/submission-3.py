class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        max_length = 0
        for num in sett:
            if num - 1 not in sett:
                length = 1
                while num + length in sett:
                    length += 1
                max_length = max(length, max_length)
        return max_length

