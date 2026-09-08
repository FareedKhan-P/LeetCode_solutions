class Solution:
    def countCommas(self, n: int) -> int:
        return max(n-999, 0)

        # count = 0
        # for i in range(1, n + 1):
        #     if i >= 1000:
        #         count += 1
        # return count