import datetime
from cli import parser
from expense import Expense

def main():
    # Load data
    Expense.import_from_csv()

    # Get CLI args
    args = parser.parse_args()

    # Execute commands
    if args.command == "add":
        expense = Expense(args.description, args.amount)

    elif args.command == "list":
        if len(Expense.expenses) == 0:
            print("No expenses saved.")
        else:
            print("# ID Date Description Amount")
            for e in Expense.expenses:
                print(f"{e.id} {e.timestamp} {e.description} {e.amount}")

    elif args.command == "delete":
        e = next((x for x in Expense.expenses if x.id == args.id), None)
        if e:
            Expense.expenses.remove(e)
            print("Expense deleted successfully")
        else:
            print(f"No expense with id {id} found.")
    
    elif args.command == "update":
        e = next((x for x in Expense.expenses if x.id == args.id), None)
        if not e:
            print(f"No expense with id {id} found.")
        else:
            modified = False
            if args.description:
                e.description = args.description
                modified = True
            if args.amount:
                e.amount = args.amount
                modified = True

            if modified:
                print("Expense updated successfully")
            else:
                print("Please pass values to update")

    elif args.command == "summary":
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
                print(f"Total expenses for ({current_year}/{args.month}): ${total}")
            else:
                print("Invalid month. Please enter value 1 - 12")

        else:
            total = 0
            for e in Expense.expenses:
                total += e.amount
            print(f"Total expenses: ${total}")
    
    # Save data
    Expense.export_to_csv()

if __name__ == "__main__":
    main()