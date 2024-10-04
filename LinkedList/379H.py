from collections import deque

class PhoneDicrectory():
    def __init__(self, maxNumbers):
        self.available = [True] * maxNumbers
        self.q = deque([i for i in range(maxNumbers)])
    
    def get(self):
        if self.q:
            self.available[self.q[0]] = False
            return self.q.popleft()
        return -1
    def check(self, number):
        return self.available[number]
    def release(self, number):
        if not self.available[number]:
            self.available[number] = True
            self.q.append(number)
            