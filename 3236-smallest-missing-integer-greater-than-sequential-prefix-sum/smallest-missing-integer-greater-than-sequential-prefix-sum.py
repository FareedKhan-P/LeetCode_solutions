class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        numSet = set(nums)
        x = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                x += nums[i]
            else:
                break
        while x in numSet:
            x += 1
        return x