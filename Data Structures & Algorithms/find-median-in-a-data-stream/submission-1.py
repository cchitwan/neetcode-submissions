class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            pop = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -pop)
        

    def findMedian(self) -> float:
        l, m = len(self.max_heap), len(self.min_heap)

        if ( l+m ) % 2 == 1:
            return -self.max_heap[0]
        else:
            return     (-self.max_heap[0] + self.min_heap[0]) /2

        
        