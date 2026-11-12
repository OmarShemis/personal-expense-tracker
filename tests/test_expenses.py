import contextlib,io,unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from decimal import Decimal
from expense import Expense,ExpenseTracker

class ExpensesTests(unittest.TestCase):
    def test_invalid_amounts(self):
        for value in ["bad","NaN","Infinity","-1","0"]:
            with self.assertRaises(ValueError): Expense("Food",value,"Meals")
    def test_persistence_and_display(self):
        with TemporaryDirectory() as folder:
            path=Path(folder)/"expenses.db"
            first=ExpenseTracker(path);first.add_expense(Expense("Lunch","12.50","Meals"))
            second=ExpenseTracker(path)
            self.assertEqual(second.expenses[0].amount,Decimal("12.50"))
            output=io.StringIO()
            with contextlib.redirect_stdout(output): second.display_expenses()
            self.assertNotIn("None",output.getvalue())
    def test_import_does_not_prompt(self):
        import main
        self.assertTrue(callable(main.main))
