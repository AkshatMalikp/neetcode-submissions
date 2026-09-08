class Solution:


    def rec(self,coins: List[int],RA: int,dp:List[List],n)->int:
        if RA<=0:
            return 0

        if n == len(coins):
           return float("inf")     


        if dp[n][RA]!=-1:
            return dp[n][RA]    
        
        if RA-coins[n]>=0:

            totalcoins=min(1+self.rec(coins,RA-coins[n],dp,n),self.rec(coins,RA,dp,n+1))

        else:
            totalcoins=self.rec(coins,RA,dp,n+1)
        dp[n][RA]=totalcoins
        return totalcoins    




    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        ans = self.rec(coins, amount, dp, 0)

        if ans == float("inf"):
            return -1

        return ans
        