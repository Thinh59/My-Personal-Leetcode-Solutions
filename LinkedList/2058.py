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
    def nodesBetweenCriticalPoints(self, head):
        lst = []
        cur = head
        while cur:
            lst.append(cur.data)
            cur = cur.next
        index = []
        for i in range(1, len(lst) - 1):
            if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
                index.append(i)
            if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
                index.append(i)
        if len(index) < 2:
            return [-1, -1]
        minD = abs(index[0] - index[1])
        maxD = index[-1] - index[0]
        for i in range(1, len(index)):
            minD = min(minD, index[i] - index[i - 1])
        return [minD, maxD]
    def nodesBetweenCriticalPointsSolve2(self, head):
        prev = head
        cur = head.next
        aft = cur.next
        index = 2
        res = []
        while aft:
            if (cur.data > prev.data and cur.data > aft.data) or (cur.data < prev.data and cur.data < aft.data):
                res.append(index)
            index = index + 1
            prev = cur
            cur = aft
            aft = aft.next
        if len(res) < 2:
            return [-1, -1]
        minD = res[1] - res[0]
        maxD = res[-1] - res[0]
        for i in range(1, len(res)):
            minD = min(minD, res[i] - res[i - 1])
        return [minD, maxD]
if __name__ == "__main__":
    lst = [5, 3, 1, 2, 5, 1, 2]
    ListNodes = LinkedList()
    ListNodes.toLinkedList(lst)
    ListNodes.printLinkedList()
    solution = Solution()
    print(solution.nodesBetweenCriticalPointsSolve2(ListNodes.head))
