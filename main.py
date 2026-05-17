from cli import parser
from expense import Expense
import expense_manager

def main():
    # Load data
    Expense.load_expenses()
    Expense.load_budgets()

    # Get CLI args
    args = parser.parse_args()

    # Handle commands
    response = expense_manager.handle_commands(args)
    if response: print(response)
    
    # Save data
    Expense.save_expenses()
    Expense.save_budgets()

if __name__ == "__main__":
    main()