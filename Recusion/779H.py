class Solution():
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        length = 2 ** (n - 1)
        half = length // 2
        if k <= half:
            return self.kthGrammar(n - 1, k)
        else:
            return self.kthGrammar(n - 1, k - half) ^ 1 #XOR với 1
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.kthGrammar(n = 3, k = 4))