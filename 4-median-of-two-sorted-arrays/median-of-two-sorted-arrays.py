class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(sorted(nums1+nums2))
        
        # l, r = 0, 0
        # arr = []
        # l1 = len(nums1)-1
        # l2 = len(nums2)-1
        # while l != l1 or r != l2:
        #     if nums1[l] <= nums2[r]:
        #         arr.append(nums1[l])
        #         l += 1
        #     else:
        #         arr.append(nums2[r])
        #         r += 1
        # if l != l1:
        #     arr.append(nums1[l1:])
        # else:
        #     arr.append(nums2[r:])
        # l_arr = len(arr)
        # if l_arr