import datetime
import csv
import os

class Expense:
    # Class Attributes
    id = 0
    expenses = []
    def __init__(self, description: str, amount: float, category: str, id: int = None, timestamp: str = None, from_csv: bool = False):
        # Validate arguments
        assert amount >= 0, f"Amount {amount} cannot be negative."

        # Assign values to self
        self.description = description
        self.amount = amount
        self.category = category if category else "Uncategorized"
        self.id = id if id is not None else Expense.create_id()
        self.timestamp = timestamp if timestamp is not None else Expense.create_timestamp()

        # Execute actions
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
        dt_obj = datetime.datetime.now()
        return dt_obj.strftime("%Y-%m-%d")
    
    @staticmethod
    def import_from_csv():
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
            Expense.id = max(e.id for e in Expense.expenses)

    @staticmethod
    def export_to_csv():
        fieldnames = ["description", "amount", "category", "id", "timestamp"]
        with open("expenses.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for expense in Expense.expenses:
                writer.writerow(vars(expense))