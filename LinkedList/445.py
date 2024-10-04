class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class ListNodes():
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
    def addTwoNumbers(self, l1, l2):
        lst1 = []
        lst2 = []
        while l1:
            lst1.append(l1.data)
            l1 = l1.next
        while l2:
            lst2.append(l2.data)
            l2 = l2.next
        n1 = 0
        n2 = 0
        p = 1
        for i in range(len(lst1) - 1, -1, -1):
            n1 = n1 + lst1[i] * p
            p = p * 10
        p = 1
        for i in range(len(lst2) - 1, -1, -1):
            n2 = n2 + lst2[i] * p
            p = p * 10
        s = n1 + n2
        result = []
        if s == 0:
            result.append(0)
        else:
            while s != 0:
                result.append(s % 10)
                s = s // 10
        res = resNext = Node(None)
        for i in result:
            resNext.next = Node(i)
            resNext = resNext.next
        return res.next
    def addTwoNumbersII(self, l1, l2):
        s1 = 0
        s2 = 0
        while l1:
            if l1 == None:
                break
            s1 = s1 * 10 + l1.val
            l1 = l1.next
        while l2:
            if l2 == None:
                break
            s2 = s2 * 10 + l2.val
            l2 = l2.next
        s = s1 + s2
        res = Node(s % 10)
        s = (s - res.val) // 10
        while s > 0:
            res = Node(s % 10, res)
            s = (s - res.val) // 10
        return res