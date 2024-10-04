class Solution():
    def predictTheWinner(self, nums):
        """
        Input: nums = [1,5,2]
        Output: false
        Explanation: Initially, player 1 can choose between 1 and 2. 
        If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
        So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
        Hence, player 1 will never be the winner and you need to return false.
        """
        def score(i, j):
            return (i <= j) and max(
                nums[i] - score(i + 1, j), 
                nums[j] - score(i, j - 1)
            )
        return len(nums) % 2 == 0 or score(0, len(nums) - 1) >= 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.predictTheWinner(nums = [1, 2, 5]))