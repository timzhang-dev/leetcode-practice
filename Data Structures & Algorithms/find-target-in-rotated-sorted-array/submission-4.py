class Solution:
    def search(self, nums: List[int], target: int) -> int:
        [1,2,3,4,5,6]
        [2,3,4,5,6,1]
        [3,4,5,6,1,2]
        [4,5,6,1,2,3]
        [5,6,1,2,3,4]
        [6,1,2,3,4,5]

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
            