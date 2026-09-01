class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maximum=0

        while i<j:
           water=(j-i)*min(heights[i],heights[j])
           maximum=max(maximum,water)

           if heights[i]>heights[j]:
                j=j-1
           else:
                i=i+1


        return maximum        



         
