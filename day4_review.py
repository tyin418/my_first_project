# Basic Python Review

# 1. Variables and Data Types
name = "Jane"
age = 33
print(f"My name is {name} and I am {age} years old.")

# 2. Function with Error Handling
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

print(divide_numbers(10, 2))  # 5.0
print(divide_numbers(10, 0))  # Error

# 3. Loop Example
for i in range(1, 6):
    print(f"Step {i} - Looping through tasks")
