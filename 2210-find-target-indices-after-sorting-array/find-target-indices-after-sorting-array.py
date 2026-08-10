class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        arr = []
        for x in range(len(nums)):
            if nums[x] == target:
                arr.append(x)
        return arr