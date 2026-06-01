class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -math.inf
        s = 0

        for n in nums:
            s += n
            ans = max(s, ans)
            if s < 0:
                s = 0
        return ans        
        