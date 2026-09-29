class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for a in range(c, amount + 1):
                dp[a] += dp[a-c]
        
        return dp[amount]
        # dp = [float('inf')] * (amount + 1)
        # dp[0] = 0
        
        # for i in range(1, amount + 1):
        #     for coin in coins:
        #         if i - coin >= 0:
        #             dp[i] = min(dp[i], 1 + dp[i - coin])
        
        # return dp[amount] if dp[amount] != float('inf') else -1