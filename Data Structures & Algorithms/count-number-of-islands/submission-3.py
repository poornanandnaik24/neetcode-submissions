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
                r, c = q.popleft()
                
                # Check neighbors: Down, Up, Right, Left
                for r, c in [(r + 1, c), (r- 1, c), (r, c+ 1), (r, c - 1)]:
                    
                    # Clean boundary check + check if it's unvisited land
                    if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0' or (r, c) in visit):
                        continue
                    q.append((r, c))
                    visit.add((r, c)) # Mark visited immediately

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
                    
        return islands