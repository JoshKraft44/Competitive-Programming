import sys

def solve():
    line = sys.stdin.readline()
    if not line: return
    numBoxes = int(line.strip())

    for _ in range(numBoxes):
        grid = []
        for j in range(3):
            row_str = sys.stdin.readline().strip()
            row = [1 if char == "*" else 0 for char in row_str]
            grid.append(row)
        
        result = min_steps(grid)
        print(result)

def flip(grid, r, c):

    for dr, dc in [(0,0), (0,1), (0,-1), (1,0), (-1,0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            grid[nr][nc] = 1 - grid[nr][nc]
    return grid

def is_solved(grid):

    for r in range(3):
        for c in range(3):
            if grid[r][c] != 0:
                return False
    return True

def min_steps(grid, steps=0):
    if is_solved(grid):
        return steps
    if steps > 9:
        return float('inf')
        
    res = float('inf')
    for r in range(3):
        for c in range(3):
            new_grid = flip(grid, r, c)
            res = min(res, min_steps(new_grid, steps + 1))
    return res

solve()
