class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        max_count = 0
        for num in sett:
            if num - 1 in sett:
                continue
            else:
                count = 0
                while num in sett:
                    count += 1
                    num += 1
                max_count = max(max_count, count)
        return max_count

