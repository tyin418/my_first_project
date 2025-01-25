# Warm-up exercises
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def power(a, b):
    return a ** b

print("Welcome to the Calculator!")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")

choice = int(input("Enter choice (1-5): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print(f"Result: {add(num1, num2)}")
elif choice == 2:
    print(f"Result: {subtract(num1, num2)}")
elif choice == 3:
    print(f"Result: {multiply(num1, num2)}")
elif choice == 4:
    print(f"Result: {divide(num1, num2)}")
elif choice == 5:
    print(f"Result: {power(num1, num2)}")
else:
    print("Invalid choice!")
