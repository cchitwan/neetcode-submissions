class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        max_heap = []
        l, m = len(nums1), len(nums2)
        if l+m == 0:
            return 0
        elif l+m == 1:
            return nums1[0] if l > 0 else nums2[0]     

        mid = (l+m)//2 # odd for odd, even for even

        i, j = 0, 0
        count = 0
        while count <= mid:
            if i < l and j < m: 
                if nums1[i] < nums2[j]:
                    heapq.heappush(max_heap, nums1[i])
                    i += 1
                else:
                    heapq.heappush(max_heap, nums2[j])
                    j += 1
            else:
                if i< l:
                    heapq.heappush(max_heap, nums1[i])
                    i += 1
                else:
                    heapq.heappush(max_heap, nums2[j])
                    j += 1
            count += 1

            if len(max_heap)> 2:
                heapq.heappop(max_heap)

        if (l+m) % 2 == 0:
            return sum(max_heap) / 2 
        else:
            heapq.heappop(max_heap)
            return max_heap[0]            

       




        

        