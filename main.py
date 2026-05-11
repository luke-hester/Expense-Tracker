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
        print("# ID Date Description Amount")
        for e in Expense.expenses:
            print(f"{e.id} {e.timestamp} {e.description} {e.amount}")
    
    # Save data
    Expense.export_to_csv()

if __name__ == "__main__":
    main()