class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True

# class Solution:
#     def uniformArray(self, nums1: list[int]) -> bool:
#         nums2 = [0] * len(nums1)
#         nums2[0] = nums1[0]
#         for x in range(1, len(nums1)):
#             nums2[x] = nums1[x-1] - nums1[x]
#         return all(num % 2 == 0 for num in nums2) or all(num % 2 != 0 for num in nums2)