class Solution:


    def answer(self,nums: List[int], target: int,n:int,summ:int,dp:List[List],total:int)->int:

        if summ==target and n==len(nums):
            return 1

        if n==len(nums) and summ!=target:
            return 0

        if dp[n][summ+total]!=-1:
            return dp[n][summ+total]





        given= self.answer(nums,target,n+1,summ+nums[n],dp,total)+self.answer(nums,target,n+1,summ-nums[n],dp,total)

        dp[n][summ+total]=given
        return given





    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)
        dp=[[-1 for _ in range(2*total+1)] for _ in range(len(nums))]
  
        return self.answer(nums,target,0,0,dp,total)
        