class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution():
    def mid(self, head):
        slow = fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next
        return slow
    
    def mid_second(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
