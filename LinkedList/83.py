class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution():
    def __init__ (self):
        self.head = None
    def toLinkedList(self, lst):
        res = resNext = ListNode()
        for i in lst:
            resNext.next = ListNode(i)
            resNext = resNext.next
        self.head = res.next
        return self.head
    def deleteDuplictaes(self):
        cur = self.head
        while cur != None and cur.next != None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return self.head
    def printLinkedList(self):
        cur = self.head
        while cur:
            print(cur.val, end = " ")
            cur = cur.next
        print()

if __name__ == "__main__":
    lst = [1, 1, 2, 3]
    LinkedList = Solution()
    LinkedList.toLinkedList(lst)
    LinkedList.printLinkedList()
    LinkedList.deleteDuplictaes()
    LinkedList.printLinkedList()