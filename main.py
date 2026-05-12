from cli import parser
from expense import Expense
import expense_manager

def main():
    # Load data
    Expense.import_from_csv()

    # Get CLI args
    args = parser.parse_args()

    # Handle commands
    response = expense_manager.handle_commands(args)
    if response: print(response)
    
    # Save data
    Expense.export_to_csv()

if __name__ == "__main__":
    main()