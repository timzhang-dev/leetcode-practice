class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        left = 0
        right = m - 1
        while left <= right:
            mid = (left + right)//2
            if target > matrix[mid][-1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                break
        
        n = len(matrix[mid])
        left = 0
        right = n - 1
        while left <= right:
            middle = (left + right)//2
            if target > matrix[mid][middle]:
                left = middle + 1
            elif target < matrix[mid][middle]:
                right = middle - 1
            else:
                return True
        return False


        
