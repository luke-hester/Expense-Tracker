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
        print(f"DEBUG: {Expense.expenses}")
        print("# ID Date Description Amount")
        for e in Expense.expenses:
            print(f"{e.id} {e.timestamp} {e.description} {e.amount}")

    elif args.command == "delete":
        e = next((x for x in Expense.expenses if x.id == args.id), None)
        if e:
            Expense.expenses.remove(e)
            print("Expense deleted successfully")
        else:
            print("No expense with id {id} found.")
        
    
    # Save data
    Expense.export_to_csv()

if __name__ == "__main__":
    main()