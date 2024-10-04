class Solution():
    def diffWaysToCompute(self, expression):
        def compute(a, b, op):
            if op == "+":
                return a + b
            if op == "-":
                return a - b
            if op == "*":
                return a * b
        res = []
        for i, char in enumerate(expression):
            if char in {"+", "-", "*"}:
                left = self.diffWaysToCompute(expression[: i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for a in left:
                    for b in right:
                        res.append(compute(a, b, char))
        if not res:
            return [int(expression)]
        
        return res
    
if __name__ == "__main__":
    expression = "2-1-1"
    sol = Solution()
    print(sol.diffWaysToCompute(expression))