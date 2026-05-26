class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        max_heap = []

        def distance_from_origin(point):
            return math.sqrt(point[0]**2 + point[1]**2)

        for point in points:
            distance =  distance_from_origin(point)
            heapq.heappush(max_heap, (-distance, point))
            if len(max_heap)> k:
                heapq.heappop(max_heap)

        return list(x[1] for x in max_heap)           
        