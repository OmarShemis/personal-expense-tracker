from contextlib import closing
"""Validated expenses with SQLite persistence."""
from dataclasses import dataclass
from decimal import Decimal,InvalidOperation,ROUND_HALF_UP
from pathlib import Path
import sqlite3

@dataclass
class Expense:
    description: str
    amount: Decimal
    category: str
    def __post_init__(self):
        self.description=self.description.strip();self.category=self.category.strip()
        if not self.description or not self.category:
            raise ValueError("Description and category are required.")
        try:
            value=Decimal(str(self.amount))
            if not value.is_finite() or value <= 0 or value > Decimal("1e15"):
                raise ValueError("Amount must be positive and finite.")
            self.amount=value.quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)
            if self.amount == 0: raise ValueError("Amount rounds to zero.")
        except InvalidOperation as error:
            raise ValueError("Enter a valid amount.") from error
    def display(self):
        return f"Description: {self.description}\nAmount: {self.amount:,.2f}\nCategory: {self.category}"

class ExpenseTracker:
    def __init__(self,database="data/expenses.db"):
        self.database=Path(database)
        self.database.parent.mkdir(parents=True,exist_ok=True)
        with closing(sqlite3.connect(self.database)) as conn, conn:
            conn.execute("CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY KEY, description TEXT, amount TEXT, category TEXT)")
    @property
    def expenses(self):
        with closing(sqlite3.connect(self.database)) as conn, conn:
            rows=conn.execute("SELECT description,amount,category FROM expenses ORDER BY id").fetchall()
        return [Expense(*row) for row in rows]
    def add_expense(self,expense):
        validated=Expense(expense.description,expense.amount,expense.category)
        with closing(sqlite3.connect(self.database)) as conn, conn:
            conn.execute("INSERT INTO expenses(description,amount,category) VALUES(?,?,?)",(validated.description,str(validated.amount),validated.category))
    def display_expenses(self):
        for expense in self.expenses:
            print(expense.display())
