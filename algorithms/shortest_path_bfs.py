from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        print(n)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        if n == 1:
            return 1

        paths = [(0,1),(1,1),(0,-1),(-1,1),(-1,-1),(-1,0),(1,0),(1,-1)]
        
        queue = deque([(0, 0, 1)])  # (row, col, distance)
        visited = set([(0, 0)])

        while queue:
            row, col, dist = queue.popleft()
            
            if row == n-1 and col == n-1:
                return dist
            
            # Explore all 8 neighbors   
            for dr, dc in paths:
                new_row, new_col = row + dr, col + dc
                
                # Check if valid and not visited
                if (0 <= new_row < n and 
                    0 <= new_col < n and 
                    grid[new_row][new_col] == 0 and
                    (new_row, new_col) not in visited):
                    
                    queue.append((new_row, new_col, dist + 1))
                    visited.add((new_row, new_col))
        
        return -1  # No path found


if __name__ == "__main__":
    sol = Solution()
    
    grid = [[0,1],[1,0]]
    expected = 2
    
    result = sol.shortestPathBinaryMatrix(grid)
    
    print(f"Input: grid = {grid}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print(f"Pass: {result == expected}")