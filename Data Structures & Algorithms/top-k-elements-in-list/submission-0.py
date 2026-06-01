class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums)
        min_heap = []

        for key,val in count_map.items():
            heapq.heappush(min_heap, (val, key))
            if len(min_heap)>k:
                heapq.heappop(min_heap)

        result = deque()
        
        while min_heap:
            _, key = heapq.heappop(min_heap)
            result.appendleft(key)

        return list(result)           
        