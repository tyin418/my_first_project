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
        return "Error: Cannot divide by zero"

print("Simple Calculator")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

try:
    choice = int(input("Choose an operation (1-4): "))
    if choice not in [1, 2, 3, 4]:
        raise ValueError("Invalid choice! Please enter a number between 1 and 4.")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print(f"User chose: {choice}, Numbers: {num1}, {num2}")

    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", subtract(num1, num2))
    elif choice == 3:
        print("Result:", multiply(num1, num2))
    elif choice == 4:
        print("Result:", divide(num1, num2))

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
