from collections import deque

def min_time_to_rot(grid):
    if not grid:
        return -1

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_oranges = 0

    # Initialize the queue with all rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_oranges += 1

    # Directions array for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    minutes_passed = 0

    # BFS
    while queue and fresh_oranges > 0:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append((nx, ny))
                    fresh_oranges -= 1
        minutes_passed += 1

    return minutes_passed if fresh_oranges == 0 else -1

# Example usage
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

print(min_time_to_rot(grid))
