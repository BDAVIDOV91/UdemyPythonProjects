import json
import os

filename = "expenses.json"

# Check if file exists, if not create it
if not os.path.exists(filename):
    with open(filename, 'w') as f:
        json.dump([], f)

# Load expenses from file
with open(filename, 'r') as f:
    try:
        expenses = json.load(f)
    except json.JSONDecodeError:
        expenses = []

# Function to add an expense
def add_expense():
    global expenses
    name = input("Enter expense name: ")
    amount = input("Enter expense amount: ")
    expenses.append({"name": name, "amount": amount})
    print("Expense added successfully!")

# Function to edit an expense
def edit_expense():
    global expenses
    print("Enter expense details to edit:")
    name = input("Expense name: ")
    amount = input("Expense amount: ")
    for expense in expenses:
        if expense["name"] == name and expense["amount"] == amount:
            new_name = input("Enter new expense name (leave blank to keep current value): ")
            if new_name != "":
                expense["name"] = new_name
            new_amount = input("Enter new expense amount (leave blank to keep current value): ")
            if new_amount != "":
                expense["amount"] = new_amount
            print("Expense edited successfully!")
            return
    print("Expense not found.")

# Function to delete an expense
def delete_expense():
    global expenses
    print("Enter expense details to delete:")
    name = input("Expense name: ")
    amount = input("Expense amount: ")
    for expense in expenses:
        if expense["name"] == name and expense["amount"] == amount:
            expenses.remove(expense)
            print("Expense deleted successfully!")
            return
    print("Expense not found.")

# Function to display expenses
def display_expenses():
    print("Expenses:")
    for expense in expenses:
        print(f"{expense['name']}: ${expense['amount']}")

# Function to save expenses to file
def save_expenses():
    with open(filename, 'w') as f:
        json.dump(expenses, f, indent=4)
    print(f"Expenses saved to {filename}")

# Main loop
while True:
    print("""
    Expense Tracker
    ---------------
    1. Add Expense
    2. Edit Expense
    3. Delete Expense
    4. Display Expenses
    5. Save Expenses to File
    6. Quit
    """)

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        edit_expense()
    elif choice == '3':
        delete_expense()
    elif choice == '4':
        display_expenses()
    elif choice == '5':
        save_expenses()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")