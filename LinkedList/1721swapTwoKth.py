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
    def swapNodes(self, k):
        if not self.head:
            return None
        fast = self.head
        slow = self.head
        first_k = None
        second_k = None

        for i in range(k - 1):
            fast = fast.next
        first_k = fast
        while fast.next:
            fast = fast.next 
            slow = slow.next
        second_k = slow
        first_k.data, second_k.data = second_k.data, first_k.data
        return self.head
    
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    ListNodes = Solution()
    ListNodes.toLinkedList(lst)
    ListNodes.printLinkedList()
    ListNodes.swapNodes(k = 2)
    ListNodes.printLinkedList()