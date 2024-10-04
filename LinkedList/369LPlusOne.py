class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def toLinkedList(self,n: int):
        n = str(n)
        l = list(n)
        res = resNext = Node(None)
        for i in range(len(l)):
            resNext.next = Node(int(l[i]))
            resNext = resNext.next
        self.head = res.next
        return self.head
    def printLinkedList(self):
        cur = self.head
        while cur:
            print(cur.data, end = " ")
            cur = cur.next
        print()
    def plusOne(self):
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.data = cur.data + 1
        return self.head
    
if __name__ == "__main__":
    n = int(input("Input n = "))
    ListNodes = LinkedList()
    ListNodes.toLinkedList(n)
    ListNodes.printLinkedList()
    ListNodes.plusOne()
    ListNodes.printLinkedList()