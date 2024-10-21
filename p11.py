def remove_k_digits(num, k):
    stack = []
    
    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # If there are still k digits left to remove
    while k > 0:
        stack.pop()
        k -= 1
    
    # Build the final number and strip leading zeros
    result = ''.join(stack).lstrip('0')
    
    return result if result else '0'

# Example usage
num = "1432219"
k = 3
print(remove_k_digits(num, k))  # Output: "1219"
