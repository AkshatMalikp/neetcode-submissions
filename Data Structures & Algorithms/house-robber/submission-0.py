class Solution:

    def rec(self,nums: List[int],n: int, dp:List[int])->int:
        if(n>len(nums)-1):
            return 0
        if(n==len(nums)-1):
            dp[n]=nums[n]
            return nums[n]    
        
        if dp[n]!=-1:
            return dp[n]


        dp[n]=nums[n]+max(self.rec(nums,n+2,dp),self.rec(nums,n+3,dp))    

        return dp[n]



    def rob(self, nums: List[int]) -> int:

        dp=[-1]*len(nums)

        return max(self.rec(nums,0,dp),self.rec(nums,1,dp))
        