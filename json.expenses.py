import json

from Track_my_expense import add_expense

def save_expenses():
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)

add_expense("24/11/2025", 50, "Food", "Lunch")
save_expenses()

def load_expenses():
    global expenses
    try:
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

load_expenses()
