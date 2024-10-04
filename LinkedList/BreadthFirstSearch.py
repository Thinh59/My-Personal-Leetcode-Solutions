class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution():
    def BFS_PerfectBinaryTree(root: TreeNode):
        if not root:
            return None
        cur = root
        nxt = root.left

        while cur and nxt:
            """
            code to solved the problem...
            """
            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        return root