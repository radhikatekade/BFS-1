# Time complexity - O(n)
# Space complexity - O(h)

# Approach - Depth First Search Recursion. Maintain a level which will equate to len(result).

from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        self.result = []
        self.dfs(root, 0)
        return self.result

    def dfs(self, root: Optional[TreeNode], lvl: int) -> None:
        # base
        if root == None:
            return
        # logic
        if lvl == len(self.result):
            temp = []
            temp.append(root.val)
            self.result.append(temp)
        else:
            self.result[lvl].append(root.val)
        
        self.dfs(root.left, lvl + 1)
        self.dfs(root.right, lvl + 1)