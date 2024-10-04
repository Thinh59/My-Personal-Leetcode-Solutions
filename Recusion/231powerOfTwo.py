class Solution():
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        return n % 2 == 0 and self.isPowerOfTwo(n // 2)

if __name__ == "__main__":
    n = int(input("Input n = "))
    solution = Solution()
    print(solution.isPowerOfTwo(n))