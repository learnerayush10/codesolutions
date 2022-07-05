# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None :
            return 0 
        if root.left == None and root.right == None:
            return 1 
        depth = 1 
        stack = [root]
        while stack:
            inner = []
            for i in range(0,len(stack)):
                current = stack[i]
                if current.left:
                    inner.append(current.left)
                    if current.left.left == None and current.left.right == None:
                        depth +=1 
                        return depth
                if current.right:
                    inner.append(current.right)
                    if current.right.left == None and current.right.right == None:
                        depth +=1 
                        return depth
            stack = inner 
            depth +=1 