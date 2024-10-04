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
    def mergeInBetween(head1, a, b, head2):
        first = Node(None)
        first.next = head1
        for i in range(a):
            first = first.next
        second = head1
        for i in range(b):
            second = second.next
        first.next = head2
        cur = head2
        while cur.next:
            cur = cur.next
        cur.next = second.next
        return head1
if __name__ == "__main__":
    lst1 = [0, 1, 2, 3, 4, 5, 6]
    lst2 = [1000, 1001, 1002, 1003, 1004]
    list1 = LinkedList()
    list1.toLinkedList(lst1)
    list1.printLinkedList()
    list2 = LinkedList()
    list2.toLinkedList(lst2)
    list2.printLinkedList()
    solution = Solution()
    Solution.mergeInBetween(head1 = list1.head, a = 2, b = 5, head2 = list2.head)
    list1.printLinkedList()