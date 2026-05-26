class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sorted_trips = sorted(trips, key = lambda x: x[1])

        min_heap = []
        total = 0
        for trip in sorted_trips:
            while min_heap and min_heap[0][0] <= trip[1]:
                to, passengers = heapq.heappop(min_heap)
                total -= passengers
            heapq.heappush(min_heap, (trip[2], trip[0]))
            total += trip[0]
            # print(min_heap, total, capacity)
            if total > capacity:
                return False            

        return True
        