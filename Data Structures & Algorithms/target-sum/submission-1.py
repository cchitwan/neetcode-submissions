class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.result = 0
        def backtrack(i, s):
            if i == len(nums):
                if s == target:
                    self.result +=1
                return

            s = s + nums[i]
            backtrack(i+1, s)

            s = s - 2*nums[i]
            backtrack(i+1, s)


        backtrack(0, 0)

        return self.result    

        