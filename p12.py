def unique_paths(m, n):
    # Create a 2D table to store results of subproblems
    dp = [[1]*n for _ in range(m)]
    
    # Fill the dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

# Example usage
m, n = 3, 7
print(unique_paths(m, n))  # Output: 28
