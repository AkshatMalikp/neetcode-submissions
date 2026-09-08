class Solution:
    def climbStairs(self, n: int) -> int:
        li=[]
        li.append(1)
        li.append(2)
        for i in range(n):
            if i==0 or i==1:
                continue
            else:
                li.append(li[i-1]+li[i-2])


        return li[n-1]            

        