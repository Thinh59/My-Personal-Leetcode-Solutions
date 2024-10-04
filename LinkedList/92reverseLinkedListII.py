class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def toLinkedList(self, lst):
        res = resNext = Node(0)
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
    
    def reverseBetween(self, left, right):
        if left > right or self.head is None:
            return self.head
        
        lst = []
        cur = self.head
        while cur:
            lst.append(cur.data)
            cur = cur.next
        if left > len(lst) or right > len(lst):
            return self.head
        left_index = left - 1
        right_index = right - 1
        lst[left_index:right_index+1] = list(reversed(lst[left_index:right_index+1]))
        print(lst)
        res = resNext = Node(0)
        for i in lst:
            resNext.next = Node(i)
            resNext = resNext.next
        self.head = res.next
        return self.head
    
if __name__ == "__main__":
    lst = [3, 5]
    ListNode = LinkedList()
    ListNode.toLinkedList(lst)
    ListNode.printLinkedList()
    ListNode.reverseBetween(left = 1, right = 2)
    ListNode.printLinkedList()