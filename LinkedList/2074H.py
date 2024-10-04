class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = Node(None)
    def toLinkedList(self, lst: list):
        res  = resNext = Node(None)
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
    def reverseEvenLengthGroups(self, head):
        lst = []
        cur = head
        while cur:
            lst.append(cur.data)
            cur = cur.next
        length = len(lst)
        group = 1
        pos = 0
        while pos < length:
            if length - pos < group + 1 and (length - pos) % 2 == 0:
                lst[pos: length] = list(reversed(lst[pos: length]))
            elif group % 2 == 0 and (min(pos + group, length) - pos) % 2 == 0:
                lst[pos: min(pos + group, length)] = list(reversed(lst[pos: min(pos + group, length)]))
            pos = pos + 1
            group = group + 1
        
        node = head
        for i in lst:
            node.data = i
            node = node.next
        return head
    
if __name__ == "__main__":
    lst = [1, 1, 0, 6, 5]
    ListNode = LinkedList()
    ListNode.toLinkedList(lst)
    ListNode.printLinkedList()
    solution = Solution()
    solution.reverseEvenLengthGroups(ListNode.head)
    ListNode.printLinkedList()

