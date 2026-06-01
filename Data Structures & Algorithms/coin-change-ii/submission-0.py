class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        dp[0][0] = 1

        r = len(coins)+1
        for i in range(1, r):
            coin = coins[i-1]
            for j in range(amount+1):
                # excluding current coin - copy no of ways from previous
                dp[i][j] = dp[i-1][j]
                # if coin can be used
                if j-coin >=0:
                    dp[i][j] += dp[i][j-coin]

        return dp[len(coins)][amount]            