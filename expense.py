class Expense:
    """
    Expense class is a simple container that holds the expense data.
    """

    def __init__(self, description: str, amount: float, category: str, id: int, timestamp: str):
        """Constructor that creates and returns object with no response message"""
        self.description = description
        self.amount = amount
        self.category = category
        self.id = id
        self.timestamp = timestamp


    @classmethod
    def create_expense(cls, description: str, amount: float, category: str, id: int, timestamp: str):
        """Factory method that returns object and response message"""
        expense_object = cls(description, amount, category, id, timestamp)
        response = f"Expense added successfully (ID: {expense_object.id})"
        return expense_object, response
    

    def __repr__(self):
        return f"{self.__class__.__name__} {self.description}, {self.amount}, {self.category}, {self.id}, {self.timestamp}"