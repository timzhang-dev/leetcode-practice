class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[right]:
                return nums[left]
            elif nums[left] > nums[right]:
                if nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid

