from expense import Expense, ExpenseTracker

tracker = ExpenseTracker()

while True:
    print("\n===== EXPENSE TRACKER ====="
          "\n1. Add expense\n"
          "2. View expenses\n"
          "3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        expense = Expense(description, amount, category)
        tracker.add_expense(expense)
        print("\nExpense added successfully!")

    elif choice == "2":
        print("\n===== YOUR EXPENSES =====")

        if not tracker.expenses:
            print("No expenses yet.")
        else:
            tracker.display_expenses()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")




