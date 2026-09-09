class Solution:
    def rec(self, nums, n, current, ans):

        if n == len(nums):
            ans.append(current.copy())
            return
        self.rec(nums, n + 1, current, ans)
        current.append(nums[n])
        self.rec(nums, n + 1, current, ans)
        current.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []

        self.rec(nums, 0, [], ans)

        return ans
   
        