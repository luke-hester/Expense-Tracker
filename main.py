from cli import parser
from expense import Expense

def main():
    args = parser.parse_args()
    print(args)

    if args.command == "add":
        expense = Expense(args.description, args.amount)
        print(expense)

if __name__ == "__main__":
    main()