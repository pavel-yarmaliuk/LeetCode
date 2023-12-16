from typing import List
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        path = self.inorderTraversal(root.left)
        path.append(root.val)
        path.extend(self.inorderTraversal(root.right))
        return path

