class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class MyLinkedList():
    def __init__(self):
        self.head = None
        self.length = 0
    def get(self, index):
        if index < 0 or index >= self.length:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.data
    def addAtHead(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.length = self.length + 1
    def addAtTail(self, val):
        cur = self.head
        if cur is None:
            self.head = Node(val)
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(val)
        self.length = self.length + 1
    def addAtIndex(self, index, val):
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            newNode = Node(val)
            newNode.next = cur.next
            cur.next = newNode
            self.length = self.length + 1
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
        self.length = self.length - 1