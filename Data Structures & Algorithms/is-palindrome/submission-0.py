class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        cleaned_text=cleaned_text.lower()
        i=0
        j=len(cleaned_text)-1


        while(i<j):
            if cleaned_text[i]==cleaned_text[j]:
                i+=1
                j-=1
            else:
                return False    



        return True
        