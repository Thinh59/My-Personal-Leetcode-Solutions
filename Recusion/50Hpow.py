class Solution():
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        
        return x * half * half

if __name__ == "__main__":
    sol = Solution()
    x = float(input("Input x = "))
    n = int(input("Input n = "))
    print(sol.myPow(x, n))