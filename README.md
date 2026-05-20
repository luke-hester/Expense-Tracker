# Expense Tracker
A command line application for managing personal expenses and budgets. Built as a submission to the [Expense Tracker project](https://roadmap.sh/projects/expense-tracker) on roadmap.sh.

## Features
- Add, update, delete expenses with descriptions, amounts and categories.
- View all expenses with optional filtering by category.
- View a spending summary for all time or a specific month.
- Set and manage monthly budgets with overspend warnings.
- CSV expense importing and exporting.

## Usage

### Expenses
```bash
python main.py add -d "Groceries" -a 45.50 -c "Food"
python main.py update --id 1 -a 50.00
python main.py delete --id 1
python main.py list
python main.py list -c "Food"
```

### Summary
```bash
python main.py summary
python main.py summary -d 2026-05
```

### Budgets
```bash
python main.py set_budget -d 2026-05 -a 500
python main.py view_budgets
python main.py delete_budget -d 2026-05
```

## Requirements
Python 3.x

No external dependencies