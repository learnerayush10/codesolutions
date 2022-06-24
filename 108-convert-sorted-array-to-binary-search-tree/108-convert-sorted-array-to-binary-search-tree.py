# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return None
        middleIndex = len(nums)//2
        returnNode = TreeNode(nums[middleIndex])
        returnNode.left,returnNode.right=self.sortedArrayToBST(nums[:middleIndex]),self.sortedArrayToBST(nums[middleIndex+1:])
        return returnNode        