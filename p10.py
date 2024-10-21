def min_path_sum(grid):
    if not grid or not grid[0]:
        return 0
    
    n, m = len(grid), len(grid[0])
    
    # Initialize the DP table
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = grid[0][0]
    
    # Fill the first row
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    
    # Fill the first column
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    
    # Fill the rest of the dp table
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    
    return dp[n - 1][m - 1]

# Example usage
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

print(min_path_sum(grid))  # Output: 7
