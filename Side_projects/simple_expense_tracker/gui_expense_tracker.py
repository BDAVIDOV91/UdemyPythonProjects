import json
import os
import tkinter as tk
from tkinter import ttk

filename = 'expenses.json'

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
    name = name_var.get()
    amount = amount_var.get()
    expenses.append({'name' : name, 'amount' : amount})
    name_var.set('')
    amount_var.set('')
    expenses_listbox.delete(0, tk.END)
    for expense in expenses:
        expenses_listbox.insert(tk.END, f"{expense['name']} : {expense['amount']}")
        save_expenses()

# Function to edit an expense
def edit_expense():
    selection = expenses_listbox.curselection()
    if selection:
        index = selection[0]
        name, amount = expenses[index]["name"], expenses[index]["amount"]
        name_var.set(name)
        amount_var.set(amount)
        expenses.pop(index)
        expenses_listbox.delete(index)
        save_expenses()

# Function to delete an expense
def delete_expense():
    selection = expenses_listbox.curselection()
    if selection:
        index = selection[0]
        expenses.pop(index)
        expenses_listbox.delete(index)
        save_expenses()

# Function to display expenses
def display_expenses():
    expenses_listbox.delete(0, tk.END)
    for expense in expenses:
        expense_name = expense['name']
        expense_amount = f"{float(expense['amount'].replace('lv', '')):,.2f}"
        expenses_listbox.insert(tk.END, f"{expense_name} : {expense_amount} лв.")

# Function to save expneses to file
def save_expenses():
    with open(filename, 'w') as f:
        json.dump(expenses, f, indent = 4)


# Greate GUI
root = tk.Tk()
root.title('Expense Tracker')

# Create input fields and labels
name_label = ttk.Label(root, text = 'Household Needs')
name_var = tk.StringVar()
name_entry = ttk.Entry(root, textvariable = name_var)
amount_label = ttk.Label(root, text = 'Amount')
amount_var = tk.StringVar()
amount_entry = ttk.Entry(root, textvariable = amount_var)

# Create buttons
add_button = ttk.Button(root, text = 'Add Expense', command = add_expense)
edit_button = ttk.Button(root, text = 'Edit Expense', command = edit_expense)
delete_button = ttk.Button(root, text = 'Delete Expense', command = delete_expense)
display_button = ttk.Button(root, text = 'Display Expense', command = display_expenses)
quit_button = ttk.Button(root, text = 'Quit', command = root.destroy)

# Create listbox to display expenses
expenses_listbox = tk.Listbox(root)
display_expenses()

# Add widgets to grid
name_label.grid(row = 0, column = 0)
name_entry.grid(row= 0, column = 1)
amount_label.grid(row = 1, column = 0)
amount_entry.grid(row =1, column = 1)
add_button.grid(row = 2, column = 0, pady = 10)
edit_button.grid(row = 2, column = 1, pady = 10)
delete_button.grid(row = 3, column = 0, pady = 10)
display_button.grid(row = 3, column = 1, pady = 10)
expenses_listbox.grid()

# Run GUI
root.mainloop()