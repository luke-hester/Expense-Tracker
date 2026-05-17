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
    if args.month:
        if 1 <= args.month <= 12:
            current_year = datetime.datetime.now().year

            total = 0
            for e in Expense.expenses:
                e_time_obj = datetime.datetime.strptime(e.timestamp, "%Y-%m-%d")
                e_year = e_time_obj.year
                e_month = e_time_obj.month
                if e_year == current_year and e_month == args.month:
                    total += e.amount
            return f"Total expenses for ({current_year}/{args.month}): ${total}"
        else:
            return "Invalid month. Please enter value 1 - 12"

    else:
        total = 0
        for e in Expense.expenses:
            total += e.amount
        return f"Total expenses: ${total:.2f}"

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
    key = f"{args.year}-{args.month:02d}"
    Expense.budgets[key] = args.budget
    return f"Budget set for {key}: ${args.budget}"

def delete_budget(args):
    key = f"{args.year}-{args.month:02d}"
    r = Expense.budgets.pop(key, None)
    return f"Budget for {key} deleted successfully" if r is not None else "Budget not found."

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

    elif args.command == "budget":
        response = set_budget(args)
    
    elif args.command == "del_budget":
        response = delete_budget(args)

    return response