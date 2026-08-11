class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxRight = -1
        for x in range(len(arr)-1, -1, -1):
            curr = arr[x]
            arr[x] = maxRight
            maxRight = max(curr, maxRight)
        return arr