class Solution:


    def lcs(self,text1: str, text2: str,dp:List[List],m:int,n:int)->int:


        if len(text1)==0 or len(text2)==0:
            return 0

        if dp[m][n]!=-1:
            return dp[m][n]


        if text1[-1]==text2[-1]:
            dp[m][n]=1+self.lcs(text1[:-1],text2[:-1],dp,m-1,n-1)
            return dp[m][n]
        else:
            dp[m][n]=max(self.lcs(text1[:-1],text2,dp,m-1,n),self.lcs(text1,text2[:-1],dp,m,n-1))
            return dp[m][n]    

        

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m=len(text1)
        n=len(text2)

        dp=[[-1 for _ in range(n)] for _ in range(m)]

        return self.lcs(text1,text2,dp,m-1,n-1)
        