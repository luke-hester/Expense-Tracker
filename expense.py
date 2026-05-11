import datetime

class Expense:
    # Class Attributes
    id = 0
    expenses = []

    def __init__(self, description: str, amount: float):
        # Validate arguments
        assert amount >= 0, f"Amount {amount} cannot be negative."

        # Assign arguments to object
        self.description = description
        self.amount = amount

        # Create values for object
        self.id = Expense.create_id()
        self.timestamp = Expense.create_timestamp()

        # Execute actions
        Expense.expenses.append(self)

        print(f"Expense added successfully (ID: {self.id})")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.description}', {self.amount}, {self.id}, {self.timestamp})"

    @classmethod
    def create_id(cls):
        cls.id += 1
        return cls.id
    
    @staticmethod
    def create_timestamp():
        dt_obj = datetime.datetime.now()
        return dt_obj.strftime("%Y-%m-%d")