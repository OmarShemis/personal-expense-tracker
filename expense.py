class Expense:
    def __init__(self, description: str, amount: float,category: str ):
        self.description = description
        self.amount = amount
        self.category = category

    def display(self):
        print(f"Description: {self.description}"
              f"\nAmount: {self.amount}"
              f"\nCategory: {self.category}"
              )

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    def add_expense(self, expense: Expense) -> None:
        self.expenses.append(expense)
    def display_expenses(self) -> None:
        for expense in self.expenses:
            print(expense.display())
