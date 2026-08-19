class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        dic={
        }
        max_len=0
        while(j<len(s)):
            
            if s[j] in dic:
                del dic[s[i]]
                i=i+1;

            elif s[j] not in dic:
                dic[s[j]]=1 
                j=j+1
                max_len=max(max_len,j-i)

        return max_len           

        