class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k > len(nums):
            return []
        result = []
        deq = deque()

        for i in range(len(nums)):
            # remove all elements from left falling out of window
            if deq and deq[0] < i-k+1:
                deq.popleft() 

            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()

            deq.append(i)

            if i>= k-1:
                result.append(nums[deq[0]])  

        return result              





        