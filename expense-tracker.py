import os
import sys
from datetime import datetime
import csv
import time
import argparse

# Global Variables:
FILE = "expenses.csv"


def on_load():
    clear_screen()
    parser = argparse.ArgumentParser(
        prog="expense-tracker.py",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=f"Welcome to the Python Expense Tracker CLI. This program was made as part of one of the projects in Roadmap.sh to learn the Python programming language.",
        epilog="Use -h for help. GitHub: Sheikh-H",
    )

    subparsers = parser.add_subparsers(required=True, dest="InitialCommand")
    add_parser = subparsers.add_parser(
        name="add",
        help="Add a new expense - 4 positional arguments [--description, --amount, --date, --category]",
    )
    add_parser.add_argument("--description", required=True, type=str)
    add_parser.add_argument("--amount", required=True, type=float)
    add_parser.add_argument("--category", required=True, type=str)
    add_parser.add_argument("--date", required=True, type=str)

    update_parser = subparsers.add_parser(
        name="update",
        help="Update an existing expense - 4 optional arguments [--id OR --description] followed by one or more of these: [--newdescription, --amount, --date, --category]",
    )
    update_parser.add_argument("--id", type=int)
    update_parser.add_argument("--description", type=str)
    update_parser.add_argument("--newdescription", type=str)
    update_parser.add_argument("--amount", type=float)
    update_parser.add_argument("--category", type=str)
    update_parser.add_argument("--date", type=str)

    view_parser = subparsers.add_parser(
        name="view",
        help="View expenses - 5 optional arguments [--id, --description, --category, --amount, --date]",
    )
    view_parser.add_argument("--description", required=False, type=str)
    view_parser.add_argument("--amount", required=False, type=float)
    view_parser.add_argument("--category", required=False, type=str)
    view_parser.add_argument("--date", required=False, type=str)
    view_parser.add_argument("--id", required=False, type=int)

    delete_parser = subparsers.add_parser(
        name="delete",
        help="Delete an expense - 1 of 2 optional arguments [--id, --description]",
    )
    delete_parser_group = delete_parser.add_mutually_exclusive_group(required=True)

    delete_parser_group.add_argument("--description", type=str)
    delete_parser_group.add_argument("--id", type=int)

    return parser, parser.parse_args()


def error_messages(*messages):
    clear_screen()
    for message in messages:
        print(message)
        time.sleep(0.5)
    time.sleep(3)
    clear_screen()
    exit()


def load_file(file=FILE):
    fieldnames = ["ID", "Date", "Description", "Amount", "Category"]
    if not os.path.exists(file):
        with open(file, "w") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, dialect="excel")
            writer.writeheader()
    with open(file, "r") as f:
        data = csv.DictReader(f, dialect="excel")
        return list(data)


def save_data(DATA, file=FILE):
    fieldnames = ["ID", "Date", "Description", "Amount", "Category"]
    with open(file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for field in DATA:
            writer.writerow(field)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def add_expense(description, amount, category, date):
    DATA = load_file()
    new_id = max(int(row["ID"]) for row in DATA) + 1 if DATA else 1

    formatted_date = datetime.strptime(date, "%d/%m/%Y").date()

    new_expense = {
        "ID": new_id,
        "Description": description,
        "Amount": amount,
        "Category": category.upper(),
        "Date": formatted_date,
    }

    DATA.append(new_expense)

    save_data(DATA, FILE)
    error_messages(
        f"Added '{description}' under '{category}' for the amount of £{amount:.2f} at {formatted_date}!"
    )


def delete_expense(expense_id, description):
    DATA = load_file()
    expense = []
    if expense_id != None:
        for i, row in enumerate(DATA):
            if int(row["ID"]) == expense_id:
                expense.append(row.copy())
                del DATA[i]
                break
    if description != None:
        counter = 0
        for i, row in enumerate(DATA):
            if str(row["Description"]).lower() == str(description).lower():
                counter += 1
        if counter == 1:
            for i, row in enumerate(DATA):
                if str(row["Description"]).lower() == description.lower():
                    expense.append(row.copy())
                    del DATA[i]
                    break
        else:
            print(
                "You have more than one expense with the same description, please use ID field instead!"
            )
            print("Here is a list of all expenses with the same description:")
            for i, row in enumerate(DATA):
                if str(row["Description"]).lower() == description.lower():
                    print("-" * 50)
                    print(f"ID: {row['ID']}\t\t\t\tDate: {row['Date']}")
                    print(f"Description: {row['Description']}")
                    print(f"Category: {row['Category']}")
                    print(f"Amount: £{row['Amount']}")
    save_data(DATA, FILE)
    if expense:
        print(f"Expense '{expense[0]['Description']}' Deleted!")
    else:
        error_messages("Unable to delete this, try again")


def update_expense(
    expense_id, description, new_description, new_amount, new_date, new_category
):
    expense_list = []
    DATA = load_file()
    if expense_id is not None and description is not None:
        error_messages(
            "Please use either expense id or expense description to search, refer to manual [-h]"
        )
    if expense_id is not None:
        for i, row in enumerate(DATA):
            if int(row["ID"]) == expense_id:
                expense_list.append(row.copy())
                if new_description != None:
                    print(row["Description"])
                    row["Description"] = new_description
                if new_amount != None:
                    row["Amount"] = new_amount
                if new_date != None:
                    formatted_date = datetime.strptime(new_date, "%d/%m/%Y").date()
                    row["Date"] = formatted_date
                if new_category != None:
                    row["Category"] = new_category
                break
    if description is not None:
        count = 0
        for row in DATA:
            if row["Description"].lower().strip() == description.lower().strip():
                count += 1
        if count > 1:
            print(
                f"You have {count} expenses with the same description, please use expense id"
            )
            print("Here is a list of all the expenses with the same description:")
            for row in DATA:
                if row["Description"].lower().strip() == description.lower().strip():
                    print("-" * 50)
                    print(f"ID: {row['ID']}\t\t\t\tDate: {row['Date']}")
                    print(f"Description: {row['Description']}")
                    print(f"Category: {row['Category']}")
                    print(f"Amount: £{row['Amount']}")
        if count == 1:
            for i, row in enumerate(DATA):
                if row["Description"].lower().strip() == description.lower().strip():
                    expense_list.append(row.copy())
                    if new_description != None:
                        row["Description"] = new_description.strip()
                    if new_amount != None:
                        row["Amount"] = new_amount
                    if new_category != None:
                        row["Category"] = new_category.strip()
                    if new_date != None:
                        formatted_date = datetime.strptime(new_date, "%d/%m/%Y").date()
                        row["Date"] = formatted_date
                    break
    save_data(DATA, FILE)
    if expense_list:
        error_messages(f"Expense '{expense_list[0]['Description']}' has been updated!")
    else:
        error_messages("Unable to update this expense, please try again!")


def view_all():
    DATA = load_file()
    clear_screen()
    print("Here is a list of all your expenses: ")
    time.sleep(2)
    for row in DATA:
        print("-" * 50)
        print(f"ID: {row['ID']}\t\t\t\tDate: {row['Date']}")
        print(f"Description: {row['Description']}")
        print(f"Category: {row['Category']}")
        print(f"Amount: £{row['Amount']}")

def view_by(description, category, month, year, day, date):
    pass


def main():
    parser, args = on_load()
    if args.InitialCommand == "add":
        if not [args.description, args.amount, args.category, args.date]:
            print(
                parser.error(
                    "Please enter all the fields needed to generate a new expense!"
                )
            )
        else:
            add_expense(args.description, args.amount, args.category, args.date)
    elif args.InitialCommand == "delete":
        if not any([args.id, args.description]):
            print(
                parser.error(
                    "Please enter the ID or description of the expense you would like to delete!"
                )
            )
        else:
            delete_expense(args.id, args.description)
    elif args.InitialCommand == "update":
        if not any(
            [
                args.amount,
                args.category,
                args.date,
                args.newdescription,
            ]
        ):
            print(
                parser.error(
                    "Please enter the fields that you would like to update for this expense!"
                )
            )
        else:
            update_expense(
                args.id,
                args.description,
                args.newdescription,
                args.amount,
                args.date,
                args.category,
            )
    elif args.InitialCommand == "view":
        if not any([args.id, args.description, args.category, args.date]):
            view_all()
        elif not any([]):
            pass


if __name__ == "__main__":
    main()


# Add an expense
# Delete an expense
# View all expenses
# View expenses for a certain month
# Add expense categories and filter by categories for view
# Export a filter output as csv file
# Export expenses as csv output
