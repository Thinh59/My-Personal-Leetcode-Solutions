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
    def pairSum(self, head):
        fast = slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            new_node = slow.next
            slow.next = prev
            prev = slow
            slow = new_node
        maxS = 0
        while slow:
            maxS = max(maxS, slow.data + prev.data)
            slow = slow.next
            prev = prev.next
        return maxS
    
    def pairSumPHCT59MTJJ(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        lst = []
        cur = head
        while cur:
            lst.append(cur.val)
            cur = cur.next
        l1 = lst[0: len(lst) // 2]
        l2 = lst[len(lst) // 2::]
        maxS = 0
        for i in range(len(l1)):
            maxS = max(maxS, l1[i] + l2[-1 - i])
        return maxS
    
if __name__ == "__main__":
    lst = [5, 4, 2, 1]
    ListNodes = LinkedList()
    ListNodes.toLinkedList(lst)
    ListNodes.printLinkedList()
    solution = Solution()
    print(solution.pairSum(ListNodes.head))