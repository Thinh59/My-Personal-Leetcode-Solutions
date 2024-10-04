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
            print(cur.data, end = "->")
            cur = cur.next
        print()
    
    def insertPos(self):
        if not self.head or not self.head.next:
            return True
        d = self.head.next.data - self.head.data
        cur = self.head
        while cur and cur.next:
            if cur.next.data - cur.data != d:
                return False
            cur = cur.next
        return True
    
    def removeNodes(self):
        res = Node(None)
        res.next = self.head
        i = res
        while i.next:
            j = i.next.next
            flag = False
            while j:
                if j.data > i.next.data:
                    flag = True
                j = j.next
            if flag:
                i.next = i.next.next
            else:
                i = i.next
        self.head = res.next
        return self.head
class Solution():
    def printLinkedList(self, head):
        cur = head
        while cur:
            print(cur.data, end = "->")
            cur = cur.next
        print()
    def mergeListC1(self, llist1, llist2):
        temp = res = Node(None)
        while llist1 and llist2:
            if llist1.data <= llist2.data:
                temp.next = llist1
                llist1 = llist1.next
            else:
                temp.next = llist2
                llist2 = llist2.next
            temp = temp.next
        temp.next = llist1 or llist2
        self.printLinkedList(res.next)
        return res.next
    def mergeList(self, llist1, llist2):
        l1 = llist1
        l2 = llist2

        # Ensure that llist1 is the list with the smallest starting node
        if l1.data > l2.data:
            l1, l2 = l2, l1

        # Use l1 as the head of the merged list
        merged_head = l1

        while l1 and l2:
            # Find the position to insert l2's node
            while l1.next and l1.next.data <= l2.data:
                l1 = l1.next

            # Swap l1 and l2
            l1.next, l2 = l2, l1.next
            l1 = l1.next
        self.printLinkedList(merged_head)
        return merged_head
    
if __name__ == "__main__":
    lst1 = [5, 6, 13]
    llist1 = LinkedList()
    llist1.toLinkedList(lst1)
    llist1.printLinkedList()
    print(llist1.insertPos())
    llist1.removeNodes()
    llist1.printLinkedList()
    lst2 = [1, 9, 15]
    llist2 = LinkedList()
    llist2.toLinkedList(lst2)
    llist2.printLinkedList()
    sol = Solution()
    sol.mergeList(llist1.head, llist2.head)
