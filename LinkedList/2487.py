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
    def removeNodes(self, head):
        if not head or not head.next:
            return head
        cur = head
        prev = None
        while cur:
            newNode = cur.next
            cur.next = prev
            prev = cur
            cur = newNode
        #cur : None, prev: đầu linked list đã đảo
        cur, prev.next = prev.next, cur  #cur = đầu linked lists, prev.next = None: tách rời prev khỏi head thành 1 linked list mới
        while cur:
            temp = cur.next
            if cur.val >= prev.val:
                cur.next = prev
                prev = cur
            cur = temp
        return prev
    
    def removeNodesPHCT59MTJJ(self, head):
        start = head
        result = []
        while start:
            end = start.next
            flat = True
            while end:
                if end.data > start.data:
                    flat = False
                end = end.next
            if flat:
                result.append(start.data)
            start = start.next
        res = resNext = Node(None)

        for i in result:
            resNext.next = Node(i)
            resNext = resNext.next
        head = res.next
        return head
    

if __name__ == "__main__":
    lst = [5, 2, 13, 3, 8]
    ListNodes = LinkedList()
    ListNodes.toLinkedList(lst)
    ListNodes.printLinkedList()
    solution = Solution()
    solution.removeNodes(ListNodes.head)
    ListNodes.printLinkedList()