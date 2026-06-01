class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = 1- obstacleGrid[0][0]
        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j>0:
                        dp[i][j] = dp[i][j-1]
                    elif j ==0 and i >0:
                        dp[i][j] = dp[i-1][j]
                    elif i != 0 and j != 0:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[rows-1][cols-1]                



