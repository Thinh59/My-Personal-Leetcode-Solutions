class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution():
    def mergeTwoLists(self, list1, list2):
        res = temp = ListNode()
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list.next
            