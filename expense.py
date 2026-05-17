import datetime
import csv
import os

class Expense:
    # Class Attributes
    id = 0
    expenses = []
    budgets = {}  # {"2026-05": 1200, "2026-06": 800} # contains only strings

    def __init__(self, description: str, amount: float, category: str, id: int = None, timestamp: str = None, from_csv: bool = False):
        # Validate arguments
        assert amount >= 0, f"Amount {amount} cannot be negative."

        # Assign values to self
        self.description = description
        self.amount = amount
        self.category = category if category else "Uncategorized"
        self.id = id if id is not None else Expense.create_id()
        self.timestamp = timestamp if timestamp is not None else Expense.create_timestamp()

        Expense.expenses.append(self)

        if not from_csv:
            print(f"Expense added successfully (ID: {self.id})")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.description}', {self.amount}, {self.category}, {self.id}, {self.timestamp})"

    @classmethod
    def create_id(cls):
        cls.id += 1
        return cls.id
    
    @staticmethod
    def create_timestamp():
        date_object = datetime.datetime.now()
        return date_object.strftime("%Y-%m-%d")
    
    @staticmethod
    def load_expenses():
        filename = "expenses.csv"
        
        if not os.path.exists(filename):
            return

        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                e = Expense(
                    description=row["description"],
                    amount=float(row["amount"]),
                    category=row["category"],
                    id=int(row["id"]),
                    timestamp=row["timestamp"],
                    from_csv=True
                    )

        if len(Expense.expenses) > 0:
            # Set the 'id' class attribute to the highest id seen
            # Prevents multiple expense objects sharing an id
            Expense.id = max(e.id for e in Expense.expenses)

    @staticmethod
    def save_expenses():
        fieldnames = ["description", "amount", "category", "id", "timestamp"]
        with open("expenses.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for expense in Expense.expenses:
                writer.writerow(vars(expense))

    @staticmethod
    def load_budgets():
        filename = "budgets.csv"
        if not os.path.exists(filename):
            return
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Expense.budgets[row["timestamp"]] = row["budget"]

    @staticmethod
    def save_budgets():
        fieldnames = ["timestamp", "budget"]
        with open("budgets.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for timestamp, budget in Expense.budgets.items():
                writer.writerow({"timestamp": timestamp, "budget": budget})

    def exceeds_budget(self):
        response = ""

        # Check if budget exists for month
        current_month = self.timestamp[:7]

        if current_month in Expense.budgets:
            monthly_budget = float(Expense.budgets[current_month])

            total_spent = sum(
                e.amount for e in Expense.expenses
                if e.timestamp.startswith(current_month)
            )

            if total_spent > monthly_budget:
                overspend = total_spent - monthly_budget
                response = f"Warning: You are €{overspend:.2f} over your {current_month} budget of €{monthly_budget:.2f}!"
            else:
                response = f"Spent: €{total_spent:.2f}/{monthly_budget:.2f} of budget for {current_month}"
        return response