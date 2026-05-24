class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numbers = sorted(set(nums))
        count = 1
        max_count = 1
        for i in range(len(numbers)-1):
            if numbers[i+1] - numbers[i] == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)
        return max_count
