"""
This is the first version of the expense tracker that I am making for one of the projects on roadmap.sh. I would like to start using other file formats as I am familiar with using SQLite and JSON already.
I will upload both copies and link them here too and should be in my repo's.

The load function and the save data function was made with the help of AI and it wasn't all that difficult to make but with CSV's having so many options. I would say that I would want to learn all the funcitons inside this method before I would say I can code comfortably with this.

>>> expense-tracker 2 link.

"""

import os
import sys
from datetime import datetime
import csv
import time

# Global Variables:
FILE = "expenses.csv"
NOW = str(datetime.now().replace(microsecond=0))


def error_messages(*messages):
    clear_screen()
    for message in messages:
        print(message)
        time.sleep(0.5)
    time.sleep(3)
    clear_screen()


def load_file(file=FILE):
    fieldnames = ["ID", "Date", "Description", "Amount"]
    if not os.path.exists(file):
        with open(file, "w") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, dialect="excel")
            writer.writeheader()
    with open(file, "r") as f:
        data = csv.DictReader(f, dialect="excel")
        return list(data)


def save_data(DATA, file=FILE):
    fieldnames = ["ID", "Date", "Description", "Amount"]
    with open(file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for field in DATA:
            writer.writerow(field)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


DATA = load_file()

# Add an expense
# Delete an expense
# View all expenses
# Veiw expenses for a certain month
# Add expense categories and filter by categories for view
# Export a filter output as csv file
# Export expenses as csv output

def add_expense(expense)

def main():
    if len(sys.argv) < 2:
        error_messages("Usage: expense-tracker.py [option] [option] [option] [option]")
    elif len(sys.argv) > 1 and sys.argv[1].lower() == 'add':
        add_expense()


if __name__ == "__main__":
    main()
