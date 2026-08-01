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

                [1,2,3,4,5,6]
                [2,3,4,5,6,1]
                [3,4,5,6,1,2]
                [4,5,6,1,2,3]
                [5,6,1,2,3,4]
                [6,1,2,3,4,5]
