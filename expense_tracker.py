expenses = []

# Function to add an expense
def add_expense(name, amount):
    expenses.append({"name": name, "amount": amount})

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for expense in expenses:
            print(f"{expense['name']}: ${expense['amount']}")

# Function to calculate total expenses
def total_expenses():
    return sum(expense['amount'] for expense in expenses)

# Main Program
print("Welcome to the Expense Tracker!")
while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Calculate Total\n4. Exit")
    
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        name = input("Enter expense name: ")
        
        try:
            amount = float(input("Enter expense amount: "))
            if amount < 0:
                print("Expense amount cannot be negative. Please try again.")
                continue
            add_expense(name, amount)
            print(f"Added: {name} - ${amount}")
        except ValueError:
            print("Invalid input! Please enter a valid number for the amount.")
    
    elif choice == 2:
        view_expenses()
    
    elif choice == 3:
        print(f"Total Expenses: ${total_expenses():.2f}")
    
    elif choice == 4:
        print("Exiting the Expense Tracker. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please choose a valid option.")
