class Solution:


    def costt(self, cost:List[int],n:int,dp:List[int])->int:

        
        

        if n==len(cost):
            return 0
        if n==len(cost)-1:
            return cost[n]

        if(dp[n]!=-1):
            return dp[n]    

        dp[n]=cost[n]+min(self.costt(cost,n+1,dp),self.costt(cost,n+2,dp))    


        return dp[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)


        return min(self.costt(cost,0,dp),self.costt(cost,1,dp))
        