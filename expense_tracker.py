# Expense Tracker - Simple and Easy to Understand
expenses = []  # List to store all expenses

def add_expense():
    """Adds a new expense to the list."""
    try:
        name = input("Enter expense name: ").strip()
        amount = float(input("Enter expense amount: "))  # Ensures valid number input
        expenses.append({"name": name, "amount": amount})
        print(f"Added: {name} - ${amount:.2f}")
    except ValueError:
        print("Invalid input! Please enter a valid number for the amount.")

def remove_expense():
    """Removes an expense by name."""
    name = input("Enter the name of the expense to remove: ").strip()
    global expenses
    original_length = len(expenses)
    expenses = [expense for expense in expenses if expense["name"].lower() != name.lower()]
    
    if len(expenses) < original_length:
        print(f"Removed expense: {name}")
    else:
        print("Expense not found!")

def view_expenses():
    """Displays all recorded expenses."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nExpense List:")
    for expense in expenses:
        print(f"- {expense['name']}: ${expense['amount']:.2f}")

def main():
    """Main loop for the expense tracker."""
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            remove_expense()
        elif choice == "3":
            view_expenses()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
