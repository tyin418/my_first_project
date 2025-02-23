try:
    amount = float(input("Enter expense amount: "))
except ValueError:
    print("Invalid input! Please enter a number.")
