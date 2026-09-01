class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       hq=[]
       for i in range(len(points)):
        distance=points[i][0]*points[i][0]+points[i][1]*points[i][1]
        distance=math.sqrt(distance)
        heapq.heappush(hq, (distance, points[i]))


       answer=[]
       for i in range(k):
        a=heapq.heappop(hq)
        answer.append(a[1])



       return answer  


             
           

        