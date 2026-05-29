# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def inorder(root, left_limit, right_limit):
            if not root:
                return True
            if left_limit<root.val<right_limit:
                left_result = inorder(root.left, left_limit, root.val)
                if not left_result:
                    return False
                return inorder(root.right, root.val, right_limit)
                
            else:
                return False

        return inorder(root, -math.inf, math.inf)                


        