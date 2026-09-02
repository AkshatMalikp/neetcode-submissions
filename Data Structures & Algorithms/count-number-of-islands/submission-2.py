class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total_islands=0

        length=len(grid)
        width=len(grid[0])


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j]=="0"):
                    continue
                else:
                    total_islands=total_islands+1
                    queue=deque()
                    queue.append([i,j])
                    grid[i][j]="0"
                    while queue:
                        [a,b]=queue.popleft()
                        if a>=0 and a<length and b>=0 and b<width:
                            if(a-1>=0 and grid[a-1][b]=="1"):
                                grid[a-1][b]="0"
                                queue.append([a-1,b])
                            
                            if(b+1<width and grid[a][b+1]=="1"):
                                grid[a][b+1]="0"
                                queue.append([a,b+1]) 
                            
                            if(a+1<length and grid[a+1][b]=="1"):
                                grid[a+1][b]="0"
                                queue.append([a+1,b])   
                            
                            if(b-1>=0 and grid[a][b-1]=="1"):
                                grid[a][b-1]="0"
                                queue.append([a,b-1])    
        return total_islands







        