"""Interactive expense tracker; importing this module never starts input."""
from expense import Expense,ExpenseTracker

def main():
    tracker=ExpenseTracker()
    while True:
        try:
            print("\nExpense Tracker\n1. Add expense\n2. View expenses\n3. Exit")
            choice=input("Choose an option: ").strip()
            if choice == "1":
                expense=Expense(input("Description: "),input("Amount: "),input("Category: "))
                tracker.add_expense(expense)
                print("Expense saved.")
            elif choice == "2":
                if tracker.expenses: tracker.display_expenses()
                else: print("No expenses yet.")
            elif choice == "3": break
            else: print("Choose 1, 2 or 3.")
        except ValueError as error: print(f"Invalid input: {error}")
        except (EOFError,KeyboardInterrupt): break
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
