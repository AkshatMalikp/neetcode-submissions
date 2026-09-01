class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq=[]

        for i in range(len(nums)):
            heapq.heappush(hq,-nums[i])


        for i in range(k-1):
            heapq.heappop(hq)



        return -heapq.heappop(hq)        



        