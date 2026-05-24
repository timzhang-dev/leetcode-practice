class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set(nums)
        return len(sett) != len(nums)