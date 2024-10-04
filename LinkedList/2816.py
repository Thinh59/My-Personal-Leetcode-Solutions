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
            resNext .next = Node(i)
            resNext = resNext.next
        self.head = res.next
        return res.next
    def printLinkedList(self):
        cur = self.head
        while cur:
            print(cur.data, end = " ")
            cur = cur.next
        print()
    def doubleIt(self):
        n = 0
        cur = self.head
        while cur:
            n = n * 10 + cur.data
            cur = cur.next
        n = list(str(n * 2))
        res = resNext = Node(None)
        for i in n:
            resNext.next = Node(i)
            resNext = resNext.next
        self.head = res.next
        return self.head
if __name__ == "__main__":
    lst = [1, 8, 9]
    listNode = LinkedList()
    listNode.toLinkedList(lst)
    listNode.printLinkedList()
    listNode.doubleIt()
    listNode.printLinkedList()