# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        if not root:
            return 0
        
        q = [root]
        k = 0
        
        while q:
            
            temp = []
            for i in q:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
                    
            q = temp
            k += 1
            
        return k