import os
import csv
import datetime
import json 
import emoji

Expense_Dir = "Expenses"
Expense_File_Json = os.path.join(Expense_Dir,"Expenses.json")
Expense_File_CSV = os.path.join(Expense_Dir,"Expenses.csv")

if not os.path.exists(Expense_Dir):
    os.makedirs(Expense_Dir)

Expenses = []

def load_expenses():
    if os.path.exists(Expense_File_Json):
        with open(Expense_File_Json , "r") as file:
            return json.load(file)
    
    return []

def save_expenses():
    if os.path.exists(Expense_File_Json):
        with open(Expense_File_Json, "w") as file:
            json.dump(Expenses , file , indent=4)

def export_to_csv():
    if Expenses:
        with open(Expense_File_CSV , "w" , newline='') as file:
            writer = csv.writer(file)
            writer.writerow("Name","Amount","Categary")
            for expenses in Expenses:
                writer.writerow(Expenses["name"],Expenses["amount"],Expenses["categary"])
            print(f"Expenses exported to {Expense_File_CSV}")
    else:
        print("No expenses to export!")

def import_from_csv():
    if os.path.exists(Expense_File_CSV):
        with open(Expense_File_CSV, "r") as file:
            reader= csv.DictReader(file)
            for row in reader:
                Expenses.append({
                    "name" : row["Name"],
                    "amount" : float(row["Amount"]),
                    "categary": row["Categary"]
                    })
        save_expenses()
        print("Expenses imported to CSV!!")
    else:
        print("CSV File not found. Please export Expenses first.")

def create_backup():
    if os.path.exists(Expenses):
        backup_name=Expense_File_Json.replace(".json","_backupfile.json")
        os.rename(Expense_File_Json, backup_name)
        print(f"Backup created : {backup_name}")

def clear_console():
    os.system("cls" if os.name =="nt" else "clear") 

def show_menu():
    

