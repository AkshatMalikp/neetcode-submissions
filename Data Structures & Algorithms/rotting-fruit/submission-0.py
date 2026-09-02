class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        length = len(grid)
        width = len(grid[0])

        queue = deque()
        fresh = 0
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                a, b = queue.popleft()
                if a - 1 >= 0 and grid[a-1][b] == 1:
                    grid[a-1][b] = 2
                    fresh -= 1
                    queue.append((a-1, b))
                if a + 1 < length and grid[a+1][b] == 1:
                    grid[a+1][b] = 2
                    fresh -= 1
                    queue.append((a+1, b))
                if b - 1 >= 0 and grid[a][b-1] == 1:
                    grid[a][b-1] = 2
                    fresh -= 1
                    queue.append((a, b-1))
                if b + 1 < width and grid[a][b+1] == 1:
                    grid[a][b+1] = 2
                    fresh -= 1
                    queue.append((a, b+1))

            time += 1

        if fresh > 0:
            return -1

        return time