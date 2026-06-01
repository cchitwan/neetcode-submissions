class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for s, val in dp.items():
                next_dp[s+num] += val
                next_dp[s-num] += val
            dp = next_dp

        return dp[target]        


    def findTargetSumWays_bt(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(i, s):
            if i == len(nums):
                if s == target:
                    return 1
                else:
                    return 0

            
            memo[(i, s)] = backtrack(i+1, s+nums[i]) + backtrack(i+1, s-nums[i])

            return memo[(i, s)]

        # return backtrack(0, 0)

         

        