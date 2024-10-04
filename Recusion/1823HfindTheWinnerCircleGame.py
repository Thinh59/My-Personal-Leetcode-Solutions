class Solution():
    def findTheWinner(self, n: int, k: int) -> int:
        def findIndex(n, k):
            if n == 1:
                return 0
            else:
                return (findIndex(n - 1, k) + k) % n
        return findIndex(n, k) + 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheWinner(n = 5, k = 2))