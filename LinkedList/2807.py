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
    def GCD(self, a, b):
        if a * b < 0:
            return -1
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return (a == 0) * b + (b == 0) * a
    def printLinkedList(self, head):
        cur = head
        while cur:
            print(cur.data, end = " ")
            cur = cur.next
        print()
    def insertGreatestCommonDivisors(self, head):
        if not head or not head.next:
            return head
        cur = head
        while cur and cur.next:
            temp = cur.next
            newNode = Node(self.GCD(cur.data, temp.data))
            cur.next = newNode
            newNode.next = temp
            cur = temp
        return head

if __name__ == "__main__":
    lst = [18, 6, 10, 3]
    ListNodes = LinkedList()
    ListNodes.toLinkedList(lst)
    ListNodes.printLinkedList()
    solution = Solution()
    solution.insertGreatestCommonDivisors(ListNodes.head)
    solution.printLinkedList(ListNodes.head)