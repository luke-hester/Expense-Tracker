import datetime
from expense import Expense

def add_expense(args):
    response = ""

    # Create expense object
    expense = Expense(args.description, args.amount, args.category)

    # Check if expense exceeds budget
    response = expense.exceeds_budget()
    
    return response

def update_expense(args):
    e = next((x for x in Expense.expenses if x.id == args.id), None)
    if not e:
        return f"No expense with id {args.id} found."
    else:
        modified = False
        if args.description:
            e.description = args.description
            modified = True
        if args.amount:
            e.amount = args.amount
            modified = True
        if args.category:
            e.category = args.category
            modified = True

        if modified:
            return "Expense updated successfully"
        else:
            return "Please pass values to update"

def delete_expense(args):
    e = next((x for x in Expense.expenses if x.id == args.id), None)
    if e:
        Expense.expenses.remove(e)
        return "Expense deleted successfully"
    else:
        return f"No expense with id {args.id} found."

def get_summary(args):
    date = args.date
    if date is None:
        # No date provided, return all time total
        total = 0
        for e in Expense.expenses:
            total += e.amount
        return f"Total expenses: ${total:.2f}"
    else:
        # Validate date
        try:
            datetime.datetime.strptime(date, "%Y-%m")
        except ValueError:
            return f"Invalid date format {date}. Expected YYYY-MM"

        # Return summary of spending for that date
        total = 0
        for e in Expense.expenses:
            e_date = e.timestamp[:7]
            if e_date == date:
                total += e.amount
        return f"Total expenses for {date}: ${total:.2f}"

def list_expenses(args):
    if len(Expense.expenses) == 0:
        return "No expenses saved."
    
    if args.filter is not None:
        expenses = [e for e in Expense.expenses if e.category == args.filter]
    else:
        expenses = Expense.expenses

    lines = ["# ID Date Category Description Amount"]
    for e in expenses:
        lines.append(f"{e.id} {e.timestamp} {e.category} {e.description} {e.amount}")

    return "\n".join(lines)

def set_budget(args):
    date = args.date
    amount = args.amount

    # Validate date
    try:
        datetime.datetime.strptime(date, "%Y-%m")
    except ValueError:
        return f"Invalid date format {date}. Expected YYYY-MM"
    
    # Validate amount
    if amount < 0:
        return f"Budget amount cannot be below 0."

    Expense.budgets[date] = amount
    return f"Budget set for {date}: ${amount:.2f}"

def delete_budget(args):
    date = args.date

    # Validate date
    try:
        datetime.datetime.strptime(date, "%Y-%m")
    except ValueError:
        return f"Invalid date format {date}. Expected YYYY-MM"

    budget = Expense.budgets.pop(date, None)
    return f"Budget for {date} deleted successfully" if budget is not None else "Budget not found."

def view_budgets(args):
    if len(Expense.budgets) < 1:
        return "No budgets set."
    
    lines = ["# Date Amount"]
    for date, amount in Expense.budgets.items():
        lines.append(f"{date} ${float(amount):.2f}")

    return "\n".join(lines)

def handle_commands(args):
    response = ""

    if args.command == "add":
        response = add_expense(args)

    elif args.command == "list":
        response = list_expenses(args)

    elif args.command == "delete":
        response = delete_expense(args)

    elif args.command == "update":
        response = update_expense(args)

    elif args.command == "summary":
        response = get_summary(args)

    elif args.command == "set_budget":
        response = set_budget(args)
    
    elif args.command == "delete_budget":
        response = delete_budget(args)

    elif args.command == "view_budgets":
        response = view_budgets(args)

    return response