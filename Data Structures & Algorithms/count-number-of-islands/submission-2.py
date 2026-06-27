import collections

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
            
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r, c)) # Mark visited immediately
            
            while q:
                row, col = q.popleft()
                
                # Check neighbors: Down, Up, Right, Left
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = row + dr, col + dc
                    
                    # Clean boundary check + check if it's unvisited land
                    if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == '0' or (nr, nc) in visit):
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc)) # Mark visited immediately

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
                    
        return islands