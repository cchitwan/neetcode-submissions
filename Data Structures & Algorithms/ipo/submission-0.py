class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        n = len(projects)
        idx = 0
        max_heap = []

        for _ in range(k):
            while idx < n and projects[idx][0] <= w:
                heapq.heappush(max_heap, -projects[idx][1])
                idx += 1
            if not max_heap:
                break

            w -= heapq.heappop(max_heap)

        return w            





        