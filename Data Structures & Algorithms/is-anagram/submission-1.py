class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictt={}
        if len(t)!=len(s):
            return False
        for x in s:
            if x in dictt:
                dictt[x]=dictt[x]+1
            else:
                dictt[x]=1
                  
        for x in t:
            if x in dictt:
                dictt[x]=dictt[x]-1
                if dictt[x] == 0:
                    dictt.pop(x)
        if len(dictt)==0:
            return True            

        return False    