import argparse

parser = argparse.ArgumentParser(
    prog="expense-tracker.py",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description="Hello w",
)

parser.add_argument(
    "add",
    type=str,
    help="Using this will help to add an expense to your data",
    choices=["add","--description", "--amount"],
)

parser.add_argument_group(
    "Adding an expense",
    "To add an expense use the following:",
)

parser.print_help()
