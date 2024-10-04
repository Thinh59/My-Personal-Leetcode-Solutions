class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def mergeKLists(self, lists : list[Node]):
        arr = []
        for l in lists:
            while l:
                arr.append(l.data)
                l = l.next
        arr.sort()
        res = Node(0)
        cur = res
        for i in arr:
            cur.next = Node(i)
            cur = cur.next
        return res.next
