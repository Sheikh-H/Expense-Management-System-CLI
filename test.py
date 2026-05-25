import datetime


input_date = input("Date : ")

format_date = datetime.datetime.strptime(input_date, "%d/%m/%Y").date()

print(format_date)