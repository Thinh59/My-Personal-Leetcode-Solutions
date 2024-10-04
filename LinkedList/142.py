class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def toLinkeList(self, lst: list):
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
    def detectCycle(self):
        cur = self.head
        nodes = set()
        while cur:
            if cur in nodes:
                return cur
            nodes.add(cur)
            cur = cur.next
        return None
    
if __name__ == "__main__":
    lst = [3,2,0,-4,2, 0]
    ListNodes = LinkedList()
    ListNodes.toLinkeList(lst)
    ListNodes.printLinkedList()
    print(ListNodes.detectCycle())