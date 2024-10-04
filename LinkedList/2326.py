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
class Solution():
    def spiralMatrix(self, m, n, head):
        a = [[-1] * n for _ in range(m)]
        c1 = 0
        c2 = n - 1
        h1 = 0
        h2 = m - 1
        cur = head
        while cur and h1 <= h2 and c1 <= c2:
            for i in range(c1, c2 + 1):
                if cur:
                    a[h1][i] = cur.data
                    cur = cur.next
            h1 = h1 + 1
            for i in range(h1, h2 + 1):
                if cur:
                    a[i][c2] = cur.data
                    cur = cur.next
            c2 = c2 - 1
            for i in range(c2, c1 - 1, -1):
                if cur:
                    a[h2][i] = cur.data
                    cur = cur.next
            h2 = h2 - 1
            for i in range(h2, h1 - 1, -1):
                if cur:
                    a[i][c1] = cur.data
                    cur = cur.next
            c1 = c1 + 1
        return a

if __name__ == "__main__":
    lst = [3,0,2,6,8,1,7,9,4,2,5,5,0]
    ListNodes = LinkedList()
    ListNodes.toLinkedList(lst)
    ListNodes.printLinkedList()
    solution = Solution()
    print(solution.spiralMatrix(m = 3, n = 5, head = ListNodes.head))