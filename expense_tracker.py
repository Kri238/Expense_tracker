import csv
src = "C:\\Users\\DELL\\OneDrive\\Documents\\Expenses.csv"


# ---------------- Functions ---------------- #

def addExpense(exp):
    with open(src, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(exp.split(","))
    print("Expense added!")


def viewExpense():
    with open(src, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def viewExpenseByCategory(cat):
    with open(src, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1].strip().lower() == cat:
                print(row)


def searchExpense(exp):
    with open(src, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3].strip().lower() == exp:
                print(row)


# ---------------- Program Menu ---------------- #

operation = input("Select an option (1-add, 2-view, 3-search): ")

if operation == "1":
    exp = input("Enter expense (date,category,amount,description): ")
    addExpense(exp)

elif operation == "2":
    viewExpense()

elif operation == "3":
    exp = input("Enter description to search: ").lower()
    searchExpense(exp)





