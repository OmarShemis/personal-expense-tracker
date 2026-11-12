# Personal Expense Tracker

A small Python CLI for recording expenses, with validated decimal amounts and local SQLite persistence.

Run `python main.py` with Python 3.11+. No external dependencies are required. Add an expense, restart the program and select View expenses to retrieve it. The database is stored at `data/expenses.db` relative to the working directory and is excluded from Git.

## Example

```text
Description: Lunch
Amount: 12.50
Category: Meals
Expense saved.
```

Run `python -m unittest discover -s tests -v`. Tests cover persistence, display, invalid values and safe module imports.

This learning project uses one currency at a time and has no authentication, multi-user support or financial-account integrations.
