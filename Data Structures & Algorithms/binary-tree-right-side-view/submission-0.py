# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        queue = []
        if not root:
            return result
        queue.append(root)
        result.append(root.val)
        next_queue = []
        while queue:
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            if next_queue:
                result.append(next_queue[-1].val)
            queue = next_queue
            next_queue = []    

        return result                
            

            


        