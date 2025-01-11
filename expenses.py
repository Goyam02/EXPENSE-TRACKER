import os
import csv
import json

Expense_Dir = "Expenses"
Expense_File_Json = os.path.join(Expense_Dir, "Expenses.json")
Expense_File_CSV = os.path.join(Expense_Dir, "Expenses.csv")

if not os.path.exists(Expense_Dir):
    os.makedirs(Expense_Dir)

Expenses = []

def load_expenses():
    if os.path.exists(Expense_File_Json):
        with open(Expense_File_Json, "r") as file:
            return json.load(file)
    return []

def save_expenses():
    with open(Expense_File_Json, "w") as file:
        json.dump(Expenses, file, indent=4)

def export_to_csv():
    if Expenses:
        with open(Expense_File_CSV, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Amount", "Category"])  # Correct header
            for expense in Expenses:
                writer.writerow([expense["name"], expense["amount"], expense["category"]])  # Correct dictionary access
        print(f"Expenses exported to {Expense_File_CSV}")
    else:
        print("No expenses to export!")

def import_from_csv():
    if os.path.exists(Expense_File_CSV):
        with open(Expense_File_CSV, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Expenses.append({
                    "name": row["Name"],
                    "amount": float(row["Amount"]),
                    "category": row["Category"]
                })
        save_expenses()
        print("Expenses imported from CSV!")
    else:
        print("CSV file not found. Please export expenses first.")

def create_backup():
    if os.path.exists(Expense_File_Json):
        backup_name = Expense_File_Json.replace(".json", "_backup.json")
        os.rename(Expense_File_Json, backup_name)
        print(f"Backup created: {backup_name}")

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def show_menu():
    print("\nExpense Tracker")
    print("1. View Expenses")
    print("2. Add Expense")
    print("3. View Expenses by Category")
    print("4. Delete Expense")
    print("5. Export Expenses to CSV")
    print("6. Import Expenses from CSV")
    print("7. Exit")

def view_expenses():
    if not Expenses:
        print("\nNo expenses recorded.")
    else:
        print("\nYour Expenses:")
        for i, expense in enumerate(Expenses, 1):
            print(f"{i}. {expense['name']} - {expense['amount']} ({expense['category']})")

def add_expense():
    name = input("Enter the expense name: ").strip()
    try:
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the expense category: ").strip()
        if name and category:
            Expenses.append({"name": name, "amount": amount, "category": category})
            save_expenses()
            print(f"Expense '{name}' added!")
        else:
            print("Expense name and category cannot be empty.")
    except ValueError:
        print("Please enter a valid amount!")

def view_by_category():
    if not Expenses:
        print("\nNo expenses recorded.")
    else:
        category = input("Enter the category to filter by: ").strip()
        filtered_expenses = [expense for expense in Expenses if expense["category"].lower() == category.lower()]
        if filtered_expenses:
            print(f"\nExpenses in Category '{category}':")
            for expense in filtered_expenses:
                print(f"- {expense['name']} - {expense['amount']}")
        else:
            print(f"No expenses found in category: '{category}'.")

def delete_expense():
    view_expenses()
    try:
        expense_num = int(input("Enter the Expense number to delete: "))
        if 1 <= expense_num <= len(Expenses):
            removed_expense = Expenses.pop(expense_num - 1)
            save_expenses()
            print(f"Expense '{removed_expense['name']}' deleted!")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    global Expenses
    Expenses = load_expenses()
    while True:
        show_menu()
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                view_expenses()
            elif choice == 2:
                add_expense()
            elif choice == 3:
                view_by_category()
            elif choice == 4:
                delete_expense()
            elif choice == 5:
                export_to_csv()
            elif choice == 6:
                import_from_csv()
            elif choice == 7:
                create_backup()
                save_expenses()
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()