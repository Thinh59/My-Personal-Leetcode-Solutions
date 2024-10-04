class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution():
    def __init__(self):
        self.head = None
    def toLinkedList(self, lst: list):
        res = resNext = Node
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
    def splitsToParts(self, k: int):
        cur = self.head
        length = 0
        while cur:
            length = length + 1
            cur = cur.next
        chunk_size = length // k
        longer_chunks = length % k
        res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)
        cur = self.head
        prev = None
        for index, num in enumerate(res):
            if prev:
                prev.next = None
            res[index] = cur
            for i in range(num):
                prev = cur
                cur = cur.next
        return res

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6]
    k = 4
    ListNodes = Solution()
    ListNodes.toLinkedList(lst)
    ListNodes.printLinkedList()
    ListNodes.splitsToParts(k)
    print(ListNodes.splitsToParts(k))
