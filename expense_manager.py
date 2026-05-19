import datetime
import os
import csv

from expense import Expense


class ExpenseManager:
    """
    Manages: handling command line args, creating/updating/deleting expenses, Saving/loading data, managing budgets.
    """

    def __init__(self):
        self.id = 0
        self.expenses = [] # [Expense('Netflix', 23.0, Entertainment, 1, 2026-05-12)] # holds the Expense instances
        self.budgets = {}  # {"2026-05": 1200, "2026-06": 800} # contains {str: float} pairs


    # ----- ExpenseManager methods ----- #
    def create_id(self):
        """Increments id counter"""
        self.id += 1
        return self.id
    

    @staticmethod
    def create_timestamp():
        """Creates a new timestamp"""
        date_object = datetime.datetime.now()
        return date_object.strftime("%Y-%m-%d")
    

    def exceeds_budget(self, expense):
        """Checks if expense exceeds budget for month created. If a budget exists"""
        current_month = expense.timestamp[:7]

        if current_month in self.budgets:
            monthly_budget = float(self.budgets[current_month])

            total_spent = sum(
                e.amount for e in self.expenses
                if e.timestamp.startswith(current_month)
            )

            if total_spent > monthly_budget:
                overspend = total_spent - monthly_budget
                return f"Warning: You are €{overspend:.2f} over your {current_month} budget of €{monthly_budget:.2f}!"
            else:
                return f"Spent: €{total_spent:.2f}/€{monthly_budget:.2f} of budget for {current_month}"


    # ----- Command methods ----- #
    def handle(self, args):
        """Runs the relevent method based on args"""
        if args.command == "add":
            response = self.add_expense(args)

        elif args.command == "list":
            response = self.list_expenses(args)

        elif args.command == "delete":
            response = self.delete_expense(args)

        elif args.command == "update":
            response = self.update_expense(args)

        elif args.command == "summary":
            response = self.get_summary(args)

        elif args.command == "set_budget":
            response = self.set_budget(args)
        
        elif args.command == "delete_budget":
            response = self.delete_budget(args)

        elif args.command == "view_budgets":
            response = self.view_budgets(args)

        return response
    

    def add_expense(self, args):
        """Creates a new user added expense and checks if it exceeds budget"""
        response_list = []

        # Validate args
        if args.amount <= 0: raise ValueError(f"Amount {args.amount} must be greater than 0")
        category = args.category if args.category and not args.category.isspace() else "Uncategorized"

        # Create values
        id = self.create_id()
        timestamp = self.create_timestamp()

        # Create expense object using the factory function
        expense, response = Expense.create_expense(args.description, args.amount, category, id, timestamp)
        self.expenses.append(expense)
        if response: response_list.append(response)

        # Check if expense exceeds budget
        response = self.exceeds_budget(expense)
        if response: response_list.append(response)
        
        return response_list


    def update_expense(self, args):
        """Updates the attributes of the specified expense"""
        expense = next((e for e in self.expenses if e.id == args.id), None)

        if not expense:
            return f"No expense with id {args.id} found."
        else:
            # Validate args similar to add_expense()
            if args.amount <= 0: raise ValueError(f"Amount {args.amount} must be greater than 0")
            category = args.category if args.category and not args.category.isspace() else "Uncategorized"

            modified = False
            if args.description:
                expense.description = args.description
                modified = True
            if args.amount:
                expense.amount = args.amount
                modified = True
            if args.category:
                expense.category = category
                modified = True

            if modified:
                return "Expense updated successfully"
            else:
                return "Please pass values to update"


    def delete_expense(self, args):
        """Deletes the specified expense"""
        expense = next((x for x in self.expenses if x.id == args.id), None)

        if expense:
            self.expenses.remove(expense)
            return "Expense deleted successfully"
        else:
            return f"No expense with id {args.id} found."


    def get_summary(self, args):
        """Returns total spending for specified month, or all time total."""
        date = args.date

        if date is None:
            # No date provided, return all time total
            total = 0
            for expense in self.expenses:
                total += expense.amount
            return f"Total expenses: €{total:.2f}"
        else:
            # Validate date
            try:
                datetime.datetime.strptime(date, "%Y-%m")
            except ValueError:
                return f"Invalid date format {date}. Expected YYYY-MM"

            # Return summary of spending for that date
            total = 0
            for expense in self.expenses:
                expense_date = expense.timestamp[:7]
                if expense_date == date:
                    total += expense.amount
            return f"Total expenses for {date}: €{total:.2f}"


    def list_expenses(self, args):
        """Lists all expenses saved, if any. Can filter by category."""
        if len(self.expenses) == 0:
            return "No expenses saved."
        
        if args.category is not None:
            # List only expenses that have the given category
            expenses = [e for e in self.expenses if e.category == args.category]
        else:
            # No category given, list all expenses
            expenses = self.expenses

        lines = ["# ID Date Category Description Amount"]

        for e in expenses:
            lines.append(f"{e.id} {e.timestamp} {e.category} {e.description} {e.amount}")

        return lines


    def set_budget(self, args):
        """Sets/updates budget for a specified YYYY-MM timestamp"""
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

        self.budgets[date] = float(amount)

        return f"Budget set for {date}: €{amount:.2f}"


    def delete_budget(self, args):
        """Removes a budget for a specified YYYY-MM timestamp"""
        date = args.date

        # Validate date
        try:
            datetime.datetime.strptime(date, "%Y-%m")
        except ValueError:
            return f"Invalid date format {date}. Expected YYYY-MM"

        budget = self.budgets.pop(date, None)

        return f"Budget for {date} deleted successfully" if budget is not None else f"No budget set for {date}"


    def view_budgets(self, args):
        """Returns a list of all existing budgets."""
        if len(self.budgets) < 1:
            return "No budgets set."
        
        lines = ["# Date Amount"]

        for date, amount in self.budgets.items():
            lines.append(f"{date} €{float(amount):.2f}")

        return lines
    
    # ----- Data saving and loading ----- #
    def load(self, expenses_file, budgets_file):
        self.load_expenses(expenses_file)
        self.load_budgets(budgets_file)

    def save(self, expenses_file, budgets_file):
        self.save_expenses(expenses_file)
        self.save_budgets(budgets_file)
    
    def load_expenses(self, expenses_file):
        """
        Creates expense objects from csv file and appends them to self.expenses.
        Sets self.id to max existing id.
        """
        filename = expenses_file

        if not os.path.exists(filename):
            return

        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Calling constructor instead of factory method, no response message is created.
                expense = Expense(
                    description=row["description"],
                    amount=float(row["amount"]),
                    category=row["category"],
                    id=int(row["id"]),
                    timestamp=row["timestamp"]
                    )
                self.expenses.append(expense)

        if len(self.expenses) > 0:
            # Set self.id to max existing id
            self.id = max(e.id for e in self.expenses)


    def save_expenses(self, expenses_file):
        """Saves expenses from self.expenses to csv file"""
        fieldnames = ["description", "amount", "category", "id", "timestamp"]

        with open(expenses_file, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(vars(expense))


    def load_budgets(self, budgets_file):
        """Creates budgets from csv file and appends them to self.budgets."""
        filename = budgets_file

        if not os.path.exists(filename):
            return
        
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.budgets[row["timestamp"]] = float(row["budget"])


    def save_budgets(self, budgets_file):
        """Saves budgets from self.budgets to csv file"""
        fieldnames = ["timestamp", "budget"]

        with open(budgets_file, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for timestamp, budget in self.budgets.items():
                writer.writerow({"timestamp": timestamp, "budget": budget})