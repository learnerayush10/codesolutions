class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        in_list=[]
        if not root:
            return
        if root.left:
            in_list+=self.inorderTraversal(root.left)
        in_list.append(root.val)
        if root.right:
            in_list+=self.inorderTraversal(root.right)
        return in_list