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
            print(cur.data, end = ' ')
            cur = cur.next
        print()
    def nextLargerNodes(self):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        lst = []
        cur = self.head
        while cur:
            lst.append(cur.data)
            cur = cur.next
        for i in range(len(lst)):
            max = lst[i]
            for j in range(i + 1, len(lst)):
                if lst[j] > max:
                    max = lst[j]
                    break
            if max > lst[i]:
                lst[i] = max
            else:
                lst[i] = 0
        lst[-1] = 0
        res = resNext = Node(None)
        for i in lst:
            resNext.next = Node(i)
            resNext = resNext.next
        self.head = res.next
        return self.head
if __name__ == "__main__":
    lst = [2, 3, 1, 5]
    ListNodes = Solution()
    ListNodes.toLinkedList(lst)
    ListNodes.printLinkedList()
    ListNodes.nextLargerNodes()
    ListNodes.printLinkedList()