# Time complexity - O(n)
# Space complexity - O(n/2)

# Approach II - Breadth First Search - Maintain a queue and result array. While q is not empty, get the 
# size of the q, run a for loop, append the curr to list and keep appending curr.left and curr.right
# to q (if exist). Finally just append the list to result

from typing import Optional, List
from queue import Queue

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
        q = Queue()
        result = []
        q.put(root)

        while not q.empty():
            size = q.qsize()
            temp = []
            for i in range(size):
                curr = q.get()
                temp.append(curr.val)
                if curr.left != None:
                    q.put(curr.left)
                if curr.right != None:
                    q.put(curr.right)
            result.append(temp)
        return result