class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution():
    def flatten(self, root):
        def dfs(root):
            if not root:
                return None
            
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            while root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            last = rightTail or leftTail or root
            return last
        dfs(root)