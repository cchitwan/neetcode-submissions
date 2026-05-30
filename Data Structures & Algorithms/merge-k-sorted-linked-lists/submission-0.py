# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i, node in enumerate(lists):
            heapq.heappush(min_heap, (node.val, i, node))
        head = ListNode()
        temp = head
        while min_heap:
            _, i, node = heapq.heappop(min_heap)
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
            temp.next = node
            temp = temp.next   
        return head.next    

        