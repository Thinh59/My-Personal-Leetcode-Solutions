class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

class Solution():
    def connect(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        cur = root
        nxt = root.left

        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        return root

if __name__ == "__main__":
    # Create the nodes
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Run the connect() function
    solution = Solution()
    result = solution.connect(root)