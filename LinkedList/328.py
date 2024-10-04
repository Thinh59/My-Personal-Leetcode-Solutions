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
    def oddEvenIndexList(self):
        values = []
        cur = self.head
        while cur:
            values.append(cur.data)
            cur = cur.next
        index = 0
        for i in range(len(values)):
            if i % 2 == 0:
                values.insert(index, values.pop(i))
                index = index + 1
        res = resNext = Node(None)
        for i in values:
            resNext.next = Node(i)
            resNext = resNext.next
        self.head = res.next
        return self.head
if __name__ == "__main__":
    lst = [2, 1, 3, 5, 6, 4, 7]
    ListNodes = LinkedList()
    ListNodes.toLinkedList(lst)
    ListNodes.printLinkedList()
    ListNodes.oddEvenIndexList()
    ListNodes.printLinkedList()