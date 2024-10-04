class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def swapPairs(self):
        if self.head == None:
            return None

        cur = self.head
        while cur and cur.next:
            cur.data , cur.next.data = cur.next.data, cur.data
            cur = cur.next.next        
        
        return self.head