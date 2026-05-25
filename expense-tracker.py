import os
import sys
from datetime import datetime
import csv
import time
import argparse

# Global Variables:
FILE = "expenses.csv"
NOW = str(datetime.now().replace(microsecond=0))


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
        help="Update an existing expense - 5 optional arguments [--id, --description, --amount, --date, --category]",
    )
    update_parser.add_argument("--id", required=True, type=int)
    update_parser.add_argument("--description", type=str)
    update_parser.add_argument("--amount", type=float)
    update_parser.add_argument("--category", type=str)
    update_parser.add_argument("--date", type=str)

    view_parser = subparsers.add_parser(
        name="view",
        help="View expenses - 5 optional arguments [--id, --description, --category, --amount]",
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
        try:
            for i, row in enumerate(DATA):
                if int(row["ID"]) == expense_id:
                    expense.append(row)
                    del DATA[i]
                    break
        except Exception as e:
            print(e)
        finally:
            save_data(DATA, FILE)
            print(f"Expense '{expense[0]['Description']}' Deleted!")
    if description != None:
        try:
            counter = 0
            for i, row in enumerate(DATA):
                if str(row["Description"]).lower() == str(description).lower():
                    counter += 1
            if counter == 1:
                for i, row in enumerate(DATA):
                    if str(row["Description"]).lower() == description.lower():
                        expense.append(row)
                        del DATA[i]
                        break
            else:
                print(
                    "You have more than one expense with the same description, please use ID field instead!"
                )
                print("Here is a list of all expenses with the same description:")
                for i, row in enumerate(DATA):
                    if str(row["Description"]).lower() == description.lower():
                        print(row)
                else:
                    exit()
        except Exception as e:
            print(e)
        finally:
            save_data(DATA, FILE)
            print(f"Expense '{expense[0]['Description']}' Deleted!")


def main():
    parser, args = on_load()
    if args.InitialCommand == "add":
        if not any([args.description, args.amount, args.category, args.date]):
            print(parser.error())
        else:
            add_expense(args.description, args.amount, args.category, args.date)

    if args.InitialCommand == "delete":
        if not any([args.id, args.description]):
            print(parser.error())
        else:
            delete_expense(args.id, args.description)
    if args.InitialCommand == "update":
        pass


if __name__ == "__main__":
    main()


# Add an expense
# Delete an expense
# View all expenses
# Veiw expenses for a certain month
# Add expense categories and filter by categories for view
# Export a filter output as csv file
# Export expenses as csv output
