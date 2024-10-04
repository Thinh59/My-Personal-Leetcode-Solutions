from collections import OrderedDict
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    def removeNthFromEnd(self, n):
        cur = self.head
        dic = OrderedDict()
        while cur:
            dic[cur] = None
            cur = cur.next
        l = list(dic.keys())
        newNode = l[-n]
        cur1 = self.head
        if self.head == newNode:
            return self.head.next
        while cur1.next:
            if cur1.next == newNode:
                cur1.next = cur1.next.next
            else:
                cur1 = cur1.next
        if cur1 == newNode:
            cur1 = None
        return self.head
    
    def removeNthFromEnd_2(self, n):
        cur = self.head
        listNode = []
        while cur:
            listNode.append(cur)
            cur = cur.next
        prev_node = listNode[-n - 1]
        prev_node.next = prev_node.next.next
        return self.head
    
    def removeNthFromEnd_3(self, n):
        dummy = Node(0)
        dummy.next = self.head
        first = dummy
        second = dummy
        for _ in range(n + 1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next