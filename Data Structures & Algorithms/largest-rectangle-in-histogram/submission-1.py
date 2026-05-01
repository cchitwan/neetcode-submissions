class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        result = 0
        n = len(heights)
        for i in range(n+1):
            while stack and (i ==n or heights[stack[-1]] > heights[i]):
                height = heights[stack.pop()]
                wd = i - stack[-1] -1 if stack else i
                result = max(result, height*wd)
            stack.append(i)
        return result            