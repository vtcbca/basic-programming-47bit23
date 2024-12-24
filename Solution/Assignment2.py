def fibonacci_generator_terms(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def fibonacci_generator_max_value(max_value):
    a, b = 0, 1
    while a < max_value:
        yield a
        a, b = b, a + b

# Example usage
n_terms = 10
max_value = 100
print(f"Fibonacci sequence up to {n_terms} terms: {list(fibonacci_generator_terms(n_terms))}")
print(f"Fibonacci sequence less than {max_value}: {list(fibonacci_generator_max_value(max_value))}")
