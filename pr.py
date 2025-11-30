# ---------------------------
# 1. Function as argument
# ---------------------------
def square(x):
    return x * x

def cube(x):
    return x * x * x

def apply_func(func, value):
    # Higher-order function: takes a function as argument
    return func(value)

print("Square of 5:", apply_func(square, 5))
print("Cube of 3:", apply_func(cube, 3))

# ---------------------------
# 2. Function returning function
# ---------------------------
def power(exponent):
    def raise_to(base):
        return base ** exponent
    return raise_to

square_func = power(2)
cube_func = power(3)

print("5 squared:", square_func(5))
print("2 cubed:", cube_func(2))

# ---------------------------
# 3. Using map, filter, reduce
# ---------------------------
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map: apply function to each element
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared Numbers (map):", squared_numbers)

# filter: filter elements based on condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers (filter):", even_numbers)

# reduce: combine elements
sum_of_numbers = reduce(lambda a, b: a + b, numbers)
print("Sum of Numbers (reduce):", sum_of_numbers)

# ---------------------------
# 4. Decorators
# ---------------------------
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# ---------------------------
# 5. Combining everything
# ---------------------------
def modify_list(lst, func):
    # higher-order function: takes function as argument
    return list(map(func, lst))

nums = [1, 2, 3, 4]
print("Original List:", nums)
print("Modified List (each element squared):", modify_list(nums, lambda x: x**2))
