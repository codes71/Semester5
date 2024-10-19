def canPlaceCows(stalls, n, c, min_dist):
    count = 1
    last_position = stalls[0]
    for i in range(1, n):
        if stalls[i] - last_position >= min_dist:
            count += 1
            last_position = stalls[i]
        if count >= c:
            return True
    return False

def largestMinDistance(stalls, n, c):
    stalls.sort()
    low = 0
    high = stalls[-1] - stalls[0]
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        if canPlaceCows(stalls, n, c, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result

# Example usage:
n = 5
c = 3
stalls = [1, 2, 8, 4, 9]
print("The largest minimum distance is:", largestMinDistance(stalls, n, c))
