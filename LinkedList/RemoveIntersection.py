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
    def printLinkedList(self):
        cur = self.head
        while cur:
            print(cur.data, end = " ")
            cur = cur.next
        print()

class Solution():
    def printLinkedList(self, head):
        cur = head
        while cur:
            print(cur.data, end = " ")
            cur = cur.next
        print()
    def removeIntersection(self, head1, head2):
        res1 = Node(None)
        res2 = Node(None)
        res1.next = head1
        res2.next = head2
        l1 = res1
        l2 = res2
        while l1 and l1.next:
            while l2.next:
                if l1.next and l2.next and l1.next.data == l2.next.data:
                    l1.next = l1.next.next
                    l2.next = l2.next.next
                    print(True)
                else:
                    l2 = l2.next
            l1 = l1.next
            l2 = res2
        head1 = res1.next
        head2 = res2.next
        self.printLinkedList(head1)
        self.printLinkedList(head2)

if __name__ == "__main__":
    lst1 = [1, 2, 3, 4, 5]
    lst2 = [1, 3, 5, 7]
    llist1 = LinkedList()
    llist2 = LinkedList()
    llist1.toLinkedList(lst1)
    llist2.toLinkedList(lst2)
    llist1.printLinkedList()
    llist2.printLinkedList()
    sol = Solution()
    sol.removeIntersection(llist1.head, llist2.head)
