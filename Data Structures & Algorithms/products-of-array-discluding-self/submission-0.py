import math 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        result = []
        for i in range(len(nums)):
            prefix.append(math.prod(nums[:i]))
            suffix.append(math.prod(nums[i+1:]))
            result.append(prefix[i]*suffix[i])
        return result
