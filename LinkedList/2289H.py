class Solution():
    def totalSteps( nums):
        step = 0
        while True:
            removed = False
            new_nums = []
            i = 0
            while i < len(nums):
                if i == 0 or nums[i] >= nums[i - 1]:
                    new_nums.append(nums[i])
                else:
                    removed = True
                i = i + 1
            if not removed:
                break
            nums = new_nums
            step = step + 1
        return step
if __name__ == "__main__":
    print(Solution.totalSteps([5,3,4,4,7,6,5,11,8,5,11]))