class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()
        n = len(nums)
        def backtrack(path):
            if len(path) == n:
                result.append(path[:])
                return

            for i in range(n):
                if nums[i] not in visited:
                    path.append(nums[i])
                    visited.add(nums[i])
                    backtrack(path)
                    visited.remove(nums[i])
                    path.pop()

        backtrack([])

        return result            

        