class ListNode():
    def __init__(self, val = 0, next = None):
        self. val = val
        self.next = next

class Solution():
    def mid(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self, head):
        new_list = None
        cur = head
        while cur:
            new_node = cur.next
            cur.next = new_list
            new_list = cur
            cur = new_node
        
        return new_list
    
    def isPlaindrome(self, head):
        midHead = self.mid(head).next
        midHead = self.reverse(midHead)

        while midHead:
            if head.val != midHead.val:
                return False
            else:
                head = head.next
                midHead = midHead.next
        return True