class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
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
    def removeZeroSumSubLists(self):
        front = Node(0, self.head)
        start = front

        while start:
            s = 0
            end = start.next
            while end:
                s = s + end.data
                if s == 0:
                    start.next = end.next
                end = end.next
            start = start.next
        self.head = front.next
        return self.head
    
if __name__ == "__main__":
    lst = [1, 5, 4, 3, 8, -3, -5, 2]
    ListNodes = Solution()
    ListNodes.toLinkedList(lst)
    ListNodes.printLinkedList()
    ListNodes.removeZeroSumSubLists()
    ListNodes.printLinkedList()