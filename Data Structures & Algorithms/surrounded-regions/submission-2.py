class Solution:
    def solve(self, board: List[List[str]]) -> None:
        length=len(board)
        width=len(board[0])


        for i in range(length):
            for j in range(width):
                if(i!=0 and j!=0 and i!=length-1 and j!=width-1 ):
                    continue
                elif board[i][j]!="O":
                    continue    
                else:
                    queue=deque()
                    queue.append((i,j))
                    board[i][j]="A"
                    while queue:
                        a,b=queue.popleft()
                        if(a-1>=0 and board[a-1][b]=="O"):
                            board[a-1][b]="A"
                            queue.append((a-1,b))
                        if(b-1>=0 and board[a][b-1]=="O"):
                            board[a][b-1]="A"
                            queue.append((a,b-1))
                        if(a+1<length and board[a+1][b]=="O"):
                            board[a+1][b]="A"
                            queue.append((a+1,b))
                        if(b+1<width and board[a][b+1]=="O"):
                            board[a][b+1]="A"
                            queue.append((a,b+1))  
        for i in range(length):
            for j in range(width):
                if board[i][j]!="A":
                    board[i][j]="X"
                else:
                    board[i][j]="O"    


        return None                              




        