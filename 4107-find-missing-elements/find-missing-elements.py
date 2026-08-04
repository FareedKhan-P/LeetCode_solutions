class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        miss = []
        for x in range(min(nums), max(nums)):
            if x not in nums:
                miss.append(x)
        return miss