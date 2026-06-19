class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for src, dst, time in times:
            graph[src].append((dst, time))

        # print(graph)
        min_heap = []
        heapq.heappush(min_heap, (0, k))

        visited = set()

        while min_heap:
            # print(min_heap)
            t, nd = heapq.heappop(min_heap)
            if nd in visited:
                continue

            visited.add(nd)
            if len(visited) == n:
                return t
            for nbh, tt in graph[nd]:
                if nbh not in visited:
                    heapq.heappush(min_heap, (tt+t, nbh))    

        return -1        



        