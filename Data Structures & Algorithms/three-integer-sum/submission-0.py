class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        triplets = []
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            target = -1 * nums[i]
            while j < k:
                result = nums[j] + nums[k]
                if result < target:
                    j += 1
                elif result > target:
                    k -= 1
                elif result == target:
                    triplets.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

        return triplets


            