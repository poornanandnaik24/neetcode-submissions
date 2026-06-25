class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        ROWS = len(grid)
        COLS = len(grid[0])
        queue = collections.deque()
        
        # 1. Find all treasures and add them to the queue simultaneously
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0: # 0 represents a treasure
                    queue.append((r, c))
                    
        # 2. Multi-source BFS: expand outward from all treasures
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        distance = 1 # The first layer of water we hit will be distance 1
        
        while queue:
            # We must process the current queue by its exact length 
            # to keep track of the distance "layers" accurately.
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                # Check all 4 adjacent neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # If the neighbor is out of bounds, or NOT empty land, skip it.
                    # (Empty land is usually initialized as 2147483647 in this problem)
                    if (nr < 0 or nr >= ROWS or 
                        nc < 0 or nc >= COLS or 
                        grid[nr][nc] != 2147483647):
                        continue
                        
                    # We found empty land! Update its distance.
                    grid[nr][nc] = distance
                    # Add it to the queue to explore its neighbors later
                    queue.append((nr, nc)) 
            
            # Once a full layer is processed, increment the distance for the next layer
            distance += 1