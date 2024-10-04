class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class TreeNode():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def toLinkedList(self, lst: list):
        res = resNext = Node(None)
        for i in lst:
            resNext.next = Node(i)
            resNext = resNext.next
        
        self.head = res.next
        return self.head
    
    def printLinkedList(self):
        cur = self.head
        while cur:
            print(cur.data, end = " ")
            cur = cur.next
        print()
    def sortedListToBST(self, head):
        self.head = head
        if self.head is None:
            return None
        elif self.head.next is None:
            return TreeNode(self.head.data)
        
        slow = fast = self.head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        root = TreeNode(slow.data)            
        root.left = self.sortedListToBST(self.head)
        root.right = self.sortedListToBST(slow.next)

        return root
    