class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class MyHashSet():
    def __init__(self):
        self.head = None
    def add(self, key):
        if not self.head:
            self.head = Node(key)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(key)
    def remove(self, key):
        cur = self.head
        if self.head.data == key:
            self.head.next = self.head
            self.head = None
        else:
            while cur and cur.next:
                if cur.next.data == key:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
    def contains(self, key):
        cur = self.head
        while cur:
            if cur.data == key:
                return True
            cur = cur.next
        return False
    