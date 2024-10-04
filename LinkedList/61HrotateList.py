class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    def toLinkedList(self, lst):
        res = resNext = Node(None)
        for i in lst:
            resNext.next = Node(i)
            resNext = resNext.next
        self.head = res.next
        return self.head
    
    def rotateRight(self, k: int):
        if self.head is None or self.head.next is None or k == 0:
            return self.head
        length = 1
        cur = self.head
        while cur.next:
            cur = cur.next
            length = length + 1
        if k == length or k % length == 0:
            return self.head
        cur.next = self.head
        k = k % length
        pos = length - k
        while pos:
            cur = cur.next
            pos = pos - 1
        
        self.head = cur.next
        cur.next = None
        return self.head
    
    def printLinkedList(self):
        cur = self.head
        while cur:
            print(cur.data, end = " ")
            cur = cur.next
        print()
    
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    ll = LinkedList()
    ll.toLinkedList(lst)
    ll.printLinkedList()
    ll.rotateRight(k = 2000000000)
    ll.printLinkedList()

