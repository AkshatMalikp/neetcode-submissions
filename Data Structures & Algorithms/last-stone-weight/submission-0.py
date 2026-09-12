class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heq=[]
        for i in stones:
            heapq.heappush(heq,-i)


        while len(heq)>1:
            top=-1*heapq.heappop(heq)
            second=-1*heapq.heappop(heq)
            if ( top==second):
                continue
            if ( top > second):
                heapq.heappush(heq,-(top-second))    

        if heq:
            return -1*heapq.heappop(heq)
        return 0
        