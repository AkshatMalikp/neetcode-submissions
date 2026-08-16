class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        A={}
        for x in nums:
            if x in A.keys():
                A[x]=A[x]+1
            else:
                A[x]=1


        maxx=-1
        hea=[]

        for key,value in A.items():
            heapq.heappush(hea,(-value,key))


        answer=[]
        for x in range(k):
            value,key=heapq.heappop(hea)
            answer.append(key)




        return answer             

        