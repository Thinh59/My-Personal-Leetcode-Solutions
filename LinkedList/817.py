class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution():
    def  __init__(self):
        self.head = None
    def numComponents(self, nums):
        pointer = self.head
        prev = None
        count = 0

        while pointer:
            if pointer.data in nums:
                if not prev:
                    count = count + 1
                prev = True
            else:
                prev = False
            pointer = pointer.next
        return count
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
if __name__ == "__main__":
    lst = [0, 1, 2, 3, 4]
    nums = [1, 3, 0, 4]
    ListNodes = Solution()
    ListNodes.toLinkedList(lst)
    ListNodes.printLinkedList()
    print(ListNodes.numComponents(nums))