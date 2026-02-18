'''
Personal Budget Tracker
'''

#1. Create an empty list named transactions . 
#This global list hold all transaction records 
transactions = []     

# variable that holds the menu to be displayed 
menu_options = """ --- Personal Budget Tracker ---   
1. Add Income
2. Add Expense
3. List Transactions
4. Delete Transaction
5. View Overall Summary
6. View Summary by Category
7. Exit"""

#2. Define a function display_menu() that takes no parameters. It should print:

def display_menu():
    """prints the menu_option variable above for the personal budget tracker"""
    choice = 0
    while choice != 7:
        print(menu_options)
        #3. The application runs continuously, displaying the menu and waiting for user input until the user selects option 7.
        choice = int(input("Please enter your choice: "))
        if choice == 7:
            print("exit")
            return False       
        if choice == 2:
            add_transaction(transactions, "expense")  # calling the function add_transaction(cuurent_transactions, transaction_type) below replacing parameters
        if choice == 1:
            add_transaction(transactions, "income")   # calling the function add_transaction(cuurent_transactions, transaction_type) below eplacing parameters
        if choice == 3:
            list_transactions(transactions)
        if choice == 4:
            delete_transaction(transactions)
        if choice == 5:
            summary = calculate_summary(transactions)
            print_overall_summary(summary) 
        if choice == 6:
            print_summary_by_category(transactions)

         
"""Task 3: 
Data model for each transaction Each transaction in transactions must be a dictionary with exactly these keys:

"type" : either "Income" or "Expense"
"amount" : a positive floating-point number
"description" : a user-provided string
"category" : a user-provided string (for example Salary, Shopping)
"""

#1. Define add_transaction(current_transactions, transaction_type)
def add_transaction(current_transanctions,transaction_type):    #current_transaction: list will store transaction dictionaries. transaction_type: a string, either income or expenses
    # try was used to handle invalid input gracefully and not break my code when input is invalid.
    try: 
        #2. Prompt user for amount , description , and category        
        amount = float(input("Enter an amount: "))    
        description = input("Enter a description: ")
        category = input("Enter a category: ")
        
        if amount >= 0:
            #4. dictionary using data model & format above that stores transaction data in memory.
            data ={"type": transaction_type, "amount": amount, "description": description,"category": category}  
            current_transanctions.append(data)  
            print(current_transanctions) 
        else:
             print("Invalid amount. Please enter a positive number.")
    except:  
        #3. If value is not a positive number, input will be handled gracefully. 
        print("Please enter a positive number.")
        return False

"""Task 4: """

#1. Define list_transactions(transactions) 
def list_transactions(transactions):

# 2. If empty, print No transactions found
    if transactions == []:
        print("no transaction found")

# 3. Otherwise print each transaction with an index starting at 1 in the format
    else: 
        index = 1
        print("--- All Transactions ---")
        for transaction in transactions:
           print(f"{index} [{transaction["type"]}] - {transaction["amount"]} - {transaction["description"]} (Category: {transaction["category"]})")
           index = index + 1
 #           print(transaction)

"""Task 5: """

#1. Define delete_transaction(transactions) 
def delete_transaction(transactions):
    
#2. First display the numbered list of transactions. If there are none, tell the user this and return without further action.
    list_transactions(transactions)     # if choice is 3
    if list_transactions == 0:
        print("list of transaction empty")
        return False

#3. Prompting the user for the number of transaction to delete.
# using try & except because I want my code to be graceful and not break with a wrong input.
    try:
        transaction_to_delete = int(input("Enter transaction to delete: "))
        if transaction_to_delete <= 0:
            print("error, enter a number from the transaction list")
            return False
        else:
            delete_index = transaction_to_delete - 1  
    
            #if transaction_to_delete == str:
            #  pass               
            # if transaction_to_delete > len(transactions):
            #         #print("error, input number within range")
            # if transaction_to_delete < 0:
                    #print("error, input a positive number within range")

        #5. If valid, remove the chosen transaction and print a confirmation
            transactions.pop(delete_index)
            print(f"{list_transactions(transactions)}")
    except:
        #4. handle all non-numeric or out of range inputs with a clear error message
        print("error, enter a number from the transaction list")   


"""Task 6: """

#1. Write a pure function calculate_summary(transactions) that computes total income, total expenses, and net balance using loops. Return a dictionary with these values.
def calculate_summary(transactions): 
    total_income = 0
    total_expenses = 0
   

    print(transactions)
    for transaction in transactions:
       
        if transaction.get("type")== "income":
            total_income += float(transaction.get("amount", 0.0))
        elif transaction.get("type") == "expense":
            total_expenses += float(transaction.get ("amount", 0.0))
                
    net_balance = total_income - total_expenses
    #dictionary with computed values
    return {"total_income": total_income,"total_expenses": total_expenses,"net_balance": net_balance,}
   

#2. Write print_overall_summary(summary_data) that prints a formatted report using the values returned by calculate_summary .
def print_overall_summary(summary_data):  #summary_data: dictionary returned by calculate_summary() containing total income, total expenses, and net balance
    print(summary_data)
    print("--- Overall summary\n")
    total_income = summary_data.get("total_income",0.0)  #where 0.0 is set as a default value
    total_expenses = summary_data.get("total_expenses", 0.0) #get function is used to return a value regardless if transaction is 0 
    net_balance = summary_data.get("net_balance",0.0)

    print(f"Total Income:   £{total_income:,.2f}")
    print(f"Total Expenses: £{total_expenses:,.2f}")
    print(f"Net Balance: £{net_balance:,.2f}")
   
  
#3. Write print_summary_by_category(transactions) that calculates total expenses for each unique category and prints a formatted report. Use loops and dictionaries, not collections.Counter or similar shortcuts
def print_summary_by_category(transactions): 
    category_totals = {}
    for transaction in transactions:
        if transaction.get("type") != "expense":
            #skip other transactions like income and report expense only
            continue
        category = str(transaction.get("category", "uncategorised"))
        amount = float(transaction.get("amount", 0.0))

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    if not category_totals:
        print("No expense transactions found")
        return
    print("--- Expenses by category ---")

    for category, total in category_totals.items():
        print(f"{category}: £{total:,.2f}")
    print("------------------------")

display_menu()