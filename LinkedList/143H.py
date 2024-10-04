class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution():
    def __init__(self):
        self.head = None
    def reorderList(self):
        slow , fast = self.head, self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        pre = slow.next = None
        while second:
            temp = second.next
            second.next = pre
            pre = second
            second = temp

        first, second = self.head, pre
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2