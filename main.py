from cli import parser
from expense_manager import ExpenseManager

expenses_file = "expenses.csv"
budgets_file = "budgets.csv"

def main():
    # Create manager and load data
    manager = ExpenseManager()
    manager.load(
        expenses_file=expenses_file,
        budgets_file=budgets_file
        )

    # Get command line args
    args = parser.parse_args()

    # Print response(s)
    response = manager.handle(args)
    if response:
        if type(response) == str:
            print(response)
        elif type(response) == list:
            for r in response: print(r)

    # Save data
    manager.save(
        expenses_file=expenses_file,
        budgets_file=budgets_file
        )


if __name__ == "__main__":
    main()