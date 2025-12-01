# ------------------------------------------
# Generator Practical Program (Single File)
# ------------------------------------------

# 1. Simple Generator
def simple_generator():
    yield 1
    yield 2
    yield 3

# 2. Even Number Generator
def even_generator(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield i

# 3. Odd Number Generator
def odd_generator(n):
    for i in range(1, n+1):
        if i % 2 != 0:
            yield i

# 4. Generator for squares
def square_generator(n):
    for i in range(1, n+1):
        yield i * i

# 5. Infinite Generator Example
def infinite_counter():
    x = 1
    while True:
        yield x
        x += 1


# ------------------------------------------
# MAIN PROGRAM (Testing Generators)
# ------------------------------------------

print("\n--- Simple Generator ---")
for v in simple_generator():
    print(v)

print("\n--- Even Number Generator (1 to 10) ---")
for v in even_generator(10):
    print(v, end=" ")

print("\n\n--- Odd Number Generator (1 to 10) ---")
for v in odd_generator(10):
    print(v, end=" ")

print("\n\n--- Square Generator (1 to 5) ---")
for v in square_generator(5):
    print(v, end=" ")

print("\n\n--- Infinite Generator (First 5 Values) ---")
gen = infinite_counter()
for _ in range(5):
    print(next(gen), end=" ")
