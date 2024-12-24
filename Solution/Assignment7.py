def triangle_pattern_nested(n):
    for i in range(1, n + 1):
        for j in range(n - i):  # Print spaces
            print(" ", end="")  
        for j in range(1, 2 * i):  # Print numbers
            print(j, end=" ")
        print()

# Example usage
n = 3
triangle_pattern_nested(n)
