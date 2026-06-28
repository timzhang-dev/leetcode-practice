import math 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        n = len(nums)
        result = [1] * n
        for i in range(n):
            result[i] = result[i] * prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n-1,-1,-1):
            result[i] = result[i] * suffix
            suffix *= nums[i]
        return result