class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def toLinkedList(self, lst):
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
    
    def deleteDuplicates(self): # 1->1->1->2->2->2->2->3->4 => 3->4
        if not self.head:
            return self.head
        res = Node(None)
        res.next = self.head
        cur = res
        while cur:
            if cur.next and cur.next.next and cur.next.data == cur.next.next.data:
                temp = cur.next.next
                while temp and temp.next and temp.data == temp.next.data:
                    temp = temp.next
                cur.next = temp.next
            else:
                cur = cur.next
        self.head = res.next

    
if __name__ == "__main__":
    lst = [1, 1, 1, 2, 2, 2, 2, 3, 4]
    ListNode = LinkedList()
    ListNode.toLinkedList(lst)
    ListNode.printLinkedList()
    ListNode.deleteDuplicates()
    ListNode.printLinkedList()