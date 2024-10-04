class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def getIntersectionNode(self, headA, headB):
        set1 = set()
        while headA is not None:
            set1.add(headA)
            headA = headA.next
        
        while headB is not None:
            if headB in set1:
                return headB
            else:
                headB = headB.next
        return None