class Solution():
    def lastRemaining(self, n):
        if n == 1:
            return 1
        return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))

if __name__ == "__main__":
    sol = Solution()
    n = int(input("Input n = "))
    print(sol.lastRemaining(n))