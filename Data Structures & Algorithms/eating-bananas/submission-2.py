import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i] / mid)
            if total <= h:
                minimum_k = mid
                right = mid - 1
            else:
                left = mid + 1
        return minimum_k

            