class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None
class Solution():
    def connect(root):
        if not root:
            return None
        
        level = [root]
        while level:
            curlevel = []
            for i, node in enumerate(level):
                if i > 0:
                    level[i - 1].next = node
                if node.left:
                    curlevel.append(node.left)
                if node.right:
                    curlevel.append(node.right)
            level = curlevel
        return root
    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    root.right.right = Node(7)
    root.left.right.left = Node(4)
    P117 = Solution()
    P117.connect(root)