class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def reverseKGroup(self, k: int):
        x = [[]]
        index_x = 0
        len_index_x = 0

        while self.head:
            if len_index_x == k:
                len_index_x = 0
                index_x = index_x + 1
                x.append([])
            x[index_x].append(self.head.data)
            self.head.data = self.head.next
            len_index_x = len_index_x + 1
        
        for i in range(len(x)):
            if len(x[i]) == k:
                x[i].reverse()
        
        res = resNext = Node(0)
        for i in x:
            for j in i:
                resNext.next = Node(j)
                resNext = resNext.next
        resNext.next = None
        return res.next