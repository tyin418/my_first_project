expenses = []

# Function to add an expense
def add_expense(name, amount):
    expenses.append({"name": name, "amount": amount})
    print(f"Added expense: {name} - ${amount:.2f}")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\nYour Expenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['name']}: ${expense['amount']:.2f}")

# Function to calculate total expenses
def total_expenses():
    return sum(expense['amount'] for expense in expenses)

# Function to remove an expense
def remove_expense(name):
    global expenses
    initial_count = len(expenses)
    expenses = [expense for expense in expenses if expense['name'].lower() != name.lower()]
    if len(expenses) < initial_count:
        print(f"Removed expense: {name}")
    else:
        print(f"No expense found with the name: {name}")

# Main Program
print("Welcome to the Expense Tracker!")
while True:
    print("\nMenu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Remove Expense")
    print("5. Exit")
    
    try:
        choice = int(input("Choose an option (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        name = input("Enter expense name: ").strip()
        try:
            amount = float(input("Enter expense amount: "))
            if amount < 0:
                print("Expense amount cannot be negative. Please try again.")
                continue
            add_expense(name, amount)
        except ValueError:
            print("Invalid input! Please enter a valid number for the amount.")
    
    elif choice == 2:
        view_expenses()
    
    elif choice == 3:
        print(f"Total Expenses: ${total_expenses():.2f}")
    
    elif choice == 4:
        name = input("Enter the name of the expense to remove: ").strip()
        remove_expense(name)
    
    elif choice == 5:
        print("Exiting the Expense Tracker. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please choose a valid option.")
