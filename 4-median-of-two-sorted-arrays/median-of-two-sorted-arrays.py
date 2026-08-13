class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # return median(sorted(nums1+nums2))

        merged = nums1 + nums2
        merged.sort()
        length = len(merged)
        if length % 2 == 1:
            return (merged[length//2])
        else:
            med1 = merged[length//2 - 1]
            med2 = merged[length//2]
        return (med1+med2)/2