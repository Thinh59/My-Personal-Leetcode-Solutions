class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution():
    def reverseList(self, head):
        cur = head
        new_list = None

        while cur:
            new_node = cur.next
            cur.next = new_list
            new_list = cur
            cur = new_node
        return new_list
