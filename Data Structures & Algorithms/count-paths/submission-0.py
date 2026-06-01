class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n

        for i in range(1, m):
            curr_dp = [0]*n
            curr_dp[0] = 1
            for j in range(1, n):
                curr_dp[j] = dp[j] + curr_dp[j-1]
            dp = curr_dp

        return dp[n-1]        

        