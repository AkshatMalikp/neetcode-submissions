class Solution:
    def rec(self, nums, n, dp, end):
        if n > end:
            return 0

        if dp[n] != -1:
            return dp[n]

        dp[n] = max(
            nums[n] + self.rec(nums, n + 2, dp, end),
            self.rec(nums, n + 1, dp, end)
        )
        return dp[n]
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp1 = [-1] * n
        case1 = self.rec(nums, 0, dp1, n - 2)
        dp2 = [-1] * n
        case2 = self.rec(nums, 1, dp2, n - 1)

        return max(case1, case2)