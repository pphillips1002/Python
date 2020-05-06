income = 0
expenses = 0
expense_dict = {}


print("\t____________________________________\t")
print("\t\t  Welcome to the Personal")
print("\t\t   Budgeting System v1.0\n")
print("\t\tCreated by: Pierce Phillips")
print("\t____________________________________\t")
start = input('\tPress enter to continue...')

if income == 0:
    income = int(input("Please enter your monthly income: "))
    print(f"Your income has been set to ${income}")
    while True:
        if expenses == 0:
            record_expenses = input("Would you like to record an expense? (y/n): ")
            if record_expenses.lower() == 'y':
                expense_name = input("Enter name of the expense: ")
                expense_value = int(input("Enter the monthly cost of the expense: "))
                print(f"{expense_name} has been recorded at ${expense_value} per month.")
                expense_dict.update({expense_name: expense_value})
                print(expense_dict)
            if record_expenses.lower() == 'y':
                continue
            else:
                break
total_expenses = sum(expense_dict.values())
remaining_total = income - total_expenses

print(f"\nYour total expenses are ${total_expenses} which leaves you with ${remaining_total}.")


def savings(income):
    savings_total = 0
    savings_percentage = 0.1
    savings_total = income * savings_percentage
    return savings_total


print(f"Monthly suggested savings ${(savings(income))}.")
expense_dict.keys()
