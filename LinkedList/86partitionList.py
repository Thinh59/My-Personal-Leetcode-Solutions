class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def toLinkedList(self, lst: list):
        res = resNext = Node(0)
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

    def partition(self, x):
        #Convert to list and process
        if self.head is None:
            return self.head
        Lst = []
        cur = self.head
        while cur:
            Lst.append(cur.data)
            cur = cur.next
        pos = 0
        for i in range(len(Lst)):
            if Lst[i] < x:
                Lst.insert(pos, Lst.pop(i))
                pos = pos + 1
        print(Lst)
        Res = ResNext = Node(None)
        for i in Lst:
            ResNext.next = Node(i)
            ResNext = ResNext.next
        self.head = Res.next
        return self.head
    
    def partitionAnswer(self, x):
        #Solve with Linked List
        h1 = l1 = Node(None)
        h2 = l2 = Node(None)

        while self.head:
            if self.head.data < x:
                l1.next = self.head
                l1 = l1.next
            else:
                l2.next = self.head
                l2 = l2.next
            
            self.head = self.head.next
        l2.next = None
        l1.next = h2.next
        self.head = h1.next
        return self.head
    
if __name__ == "__main__":
    lst = [1, 4, 3, 2, 5, 2]
    ListNode = LinkedList()
    ListNode.toLinkedList(lst)
    ListNode.printLinkedList()
    ListNode.partitionAnswer(x = 3)
    ListNode.printLinkedList()
    