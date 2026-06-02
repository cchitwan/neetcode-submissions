class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = [False] * len(nums)
        nums.sort()

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i-1] == nums[i] and not visited[i-1]:
                    continue
                path.append(nums[i])
                visited[i] = True
                backtrack(path)
                path.pop()
                visited[i] = False        
                    

        backtrack([])
        return result            



        