def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
n = 5
print(f"Factorial of {n} is {factorial_iterative(n)}")
