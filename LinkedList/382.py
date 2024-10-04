import random

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution():
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
    def getRandom(self):
        cur = self.head
        values = []
        while cur:
            values.append(cur.data)
            cur = cur.next
        return random.choice(values)

if __name__ == "__main__":
    lst = [1, 2, 3]
    ListNodes = Solution()
    ListNodes.toLinkedList(lst)
    ListNodes.printLinkedList()
    print(ListNodes.getRandom())