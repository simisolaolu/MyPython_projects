# MyPython_projects
This is a collection of my practice test and assignment.
Budget_tracker.py was my first class test back in University.

# Personal Budget Tracker

## Overview

This is a simple console-based *personal Budget Tracker* written in python.
It allows a user to:

- Add income transactions (both with description and categories)
- Add expense transactions (both with description and categories)
- List all recorded transactions
- Delete a specific transaction from the list of transactions by it's number
- View an overall transaction summary (total income, total expenses, net balance)
- View a summary of expenses grouped by category

All data is stored in memory for the duration of the programme run (no files or database are used).

---

## How to Run

- *Python Version:* written with python 3.13.7
- *File name:* budget_tracker.py

From a terminal or command prompt, navigate to the folder containing budget_tracker.py and run:

```bash
python3 budget_tracker.py
```

You will see the menu and can interact with the programme using the number keys 1-7 followed by Enter.

# Assumptions and Limitations

All monetary amounts are treated as floating point numbers in pounds (£) and displayed to two decimal places.

Transactions exist only in memory. When the programme exits, all data is lost.

Category names and descriptions are taken exactly as entered (no validation beyond basic string input).

Only simple console input/output is used; no GUI or file handling.

The menu is text based and expects numeric choices from 1 to 7.

Test Plan (Key Test Cases)

Below are some of the main tests used to check correctness:

Invalid amount input (non-numeric)

Choose Add Expense, enter fifteen as the amount.

Expected: Error message "Invalid amount. Please enter a positive number." and no transaction added.

Invalid amount input (zero or negative)

Choose Add Income, enter 0 or -100.

Expected: Same error message and no transaction added.

Listing when there are no transaction

Run the programme and immediately choose list Transactions.

Expected: Message "No transactions found."

Deleting with invalid index

Add a few transactions, then choose Delete Transaction and enter a number outside the valid range or a non-numeric value.

Expected: A clear error message and no transaction is deleted.

Overall summary and category summary

Add multiple income and expense transactions across different categories.

Use View Overall Summary and View Summary by Category.

Expected: Totals match manual calculations for income, expenses, net balance, and per-category expenses.

# Task Completion Report

Task 2: Menu and Application Setup

Implemented a global transactions list to hold all transactions dictionaries.

Impmented a varaible called menu_options to hold the menu

Implemented display_menu() to print the required menu text.

Implemented a main application loop in main() that repeatedly displays the menu and waits for user input until the user chooses Exit (7).

Task 3: Adding a Categorised Transaction

Implemented add_transaction(current_transaction, transaction_type) to handle both income and expense.

Prompts for amount, description and category.

Validates that amount is a positive number; prints an error and returns without adding if invalid.

On valid input, creates a transaction dictionary with keys "type","amount", "description", and "category", append it to the list, and prints a confirmation message.

Task 4: Listing Transaction

Implemented list_transactions(transactions) to show all transaction.

Print "No transactions found." if the list is empty.

Otherwise prints a numbered list starting at 1 in the format: 
[type] - £amount - description (Category: category).

Task 5: Deleting a Transaction

Implemented delete_transaction(transactions).

First calls list_transactions(); if there are no transactions, it prints a message and returns.

Prompts the user for the number of the transaction to delete.

Handles non-numeric input and out-of-range indices with clear error messages.

If valid, removes the chosen transaction and prints a confirmation including the deleted transaction details.

Task 6: Financial Summaries

Implemented calculate_summary(transactions) as a pure function using loops (no sum()), returning a dictionary with total_income, total_expenses, and net_balance.

Implemented print_summary(summary_data) to print a formatted report of the totals.

Implemented print_summary_by_category(transactions) using loops and a dictionary (not collections.counter) to calculate total expenses for each category and print them in a formatted list. If there are no expense transactions, it prints an appropriate message.

All tasks (2-6) have been fully implemented with comments and docstrings in the source code as required in Task 1.

