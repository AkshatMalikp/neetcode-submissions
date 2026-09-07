class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count=0
        visited=[False]*n
        
        adj = [[0] * n for _ in range(n)]


        for a,b in edges:
            adj[a][b]=1
            adj[b][a]=1
        

        for i in range(len(visited)):
            if visited[i]==True:
                continue
            else:
                stack=[]
                stack.append(i)
                visited[i]=True
                count=count+1
 
                while stack:
                    u=stack.pop()
                    
                    for v in range(n):
                        if adj[u][v]==1 and visited[v]==False:
                            stack.append(v)
                            visited[v]=True





        return count         




        