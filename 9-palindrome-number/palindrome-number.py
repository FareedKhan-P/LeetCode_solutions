class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        n = 0
        arr = list(map(int, str(x)))
        for x in range(len(arr)-1, 0, -1):
            if arr[x] != arr[n]:
                return False
            n += 1
        return True