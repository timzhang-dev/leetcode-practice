class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A
        
        left = 0
        right = len(A) - 1

        total = len(A) + len(B)
        half = total // 2
        
        while True:
            mid = (left + right) // 2
            Aleft = A[mid] if mid >= 0 else float("-infinity")
            Aright = A[mid+1] if (mid+1) < len(A) else float("infinity")
            Bleft = B[half-mid-2] if (half-mid-2) >= 0 else float("-infinity")
            Bright = B[half-mid-1] if (half-mid-1) < len(B) else float("infinity")
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                right = mid - 1
            else:
                left = mid + 1
