class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * ( amount+1)
        if amount == 0:
            return 0
        dp[0] = 0

        for coin in sorted(coins):
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[amount] if dp[amount] != math.inf else -1

            



        