class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class Solution():
    def hasCycle(self, head):
        cur = head
        seen = set()
        while cur != None:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False