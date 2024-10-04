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
    def deleteMidle(self, head):
        if not head or not head.next:
            return None
        prev = fast = slow = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = prev.next.next
        return head
    
if __name__ == "__main__":
    lst = [1, 3, 4, 7, 1, 2, 6]
    ListNodes = LinkedList()
    ListNodes.toLinkedList(lst)
    ListNodes.printLinkedList()
    solution = Solution()
    solution.deleteMidle(ListNodes.head)
    ListNodes.printLinkedList()