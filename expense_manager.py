import datetime
from expense import Expense

def add_expense(args):
    Expense(args.description, args.amount, args.category)

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
        return f"Total expenses: ${total}"

def list_expenses(args):
    if len(Expense.expenses) == 0:
        return "No expenses saved."
    
    lines = ["# ID Date Category Description Amount"]
    
    for e in Expense.expenses:
        lines.append(f"{e.id} {e.timestamp} {e.category} {e.description} {e.amount}")

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

    return response