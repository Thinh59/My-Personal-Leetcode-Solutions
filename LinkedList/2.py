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
    def twoSum(self, l1, l2):
        res = cur = Node(None)
        carry = 0

        while l1 or l2 or carry != 0:
            sum = carry
            if l1:
                sum = sum + l1.data
                l1 = l1.next
            if l2:
                sum = sum + l2.data
                l2 = l2.next
            cur.next = Node(sum % 10)
            cur = cur.next
            carry = sum // 10
        self.printLinkedList(res.next)
        return res.next
    
    def twoSum_byme(self, l1, l2):
        n1 = 0
        n2 = 0
        p = 1
        while l1:
            n1 = n1 + l1.data * p
            p = p * 10
            l1 = l1.next
        p = 1
        while l2:
            n2 = n2 + l2.data * p
            p = p * 10
            l2 = l2.next

        s = n1 + n2
        s = list(str(s))
        res = resNext = Node(None)
        for i in range(len(s) - 1, -1, -1):
            resNext.next = Node(s[i])
            resNext = resNext.next
        self.printLinkedList(res.next)
        return res.next

if __name__ == "__main__":
    lst1 = [2, 4, 3]
    lst2 = [5, 6, 4]
    l1 = LinkedList()
    l2 = LinkedList()
    l1.toLinkedList(lst1)
    l2.toLinkedList(lst2)
    l1.printLinkedList()
    l2.printLinkedList()
    sol = Solution()
    sol.twoSum_byme(l1.head, l2.head)