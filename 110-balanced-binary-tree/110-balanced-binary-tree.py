# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      
      
      
        def HeightBalance(root):
          
          if root:
            h_l,h_r = HeightBalance(root.left),HeightBalance(root.right)
            if h_l!=-1 and h_r!=-1 and abs(h_l-h_r)<=1:
              return 1+max(h_l,h_r)
            return -1
          else:
            return 1
          
        return HeightBalance(root)!=-1        