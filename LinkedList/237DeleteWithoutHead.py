class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
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
    def deleteNode(self, node):
        node.data = node.next.data
        node.next = node.next.next

if __name__ == "__main__":
    lst = [1, 4, 5, 2, 3]
    ListNodes = LinkedList()
    ListNodes.toLinkedList(lst)
    ListNodes.printLinkedList()
    ListNodes.deleteNode(Node(4))
    ListNodes.printLinkedList()
