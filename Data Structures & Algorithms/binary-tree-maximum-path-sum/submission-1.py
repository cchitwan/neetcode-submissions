# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.result = -math.inf
        def postorder(root):
            if not root:
                return 0
            val = root.val
            left_val = postorder(root.left)
            right_val = postorder(root.right)

            self.result = max(self.result, val, val+left_val+right_val , val+max(left_val, right_val))
            return max(val, val+max(left_val, right_val))

        postorder(root)
        return self.result    
        