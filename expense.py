"""
Expense tracker program for brushing up on python skills.
This program will utilize Basic Python syntax (variables, loops, functions)
Working with lists and dictionaries
File handling (reading and writing)
String formatting and user input
Error handling.
11/01/2024

"""
#List to store expenses
expenses = []

def add_expense():
    print("You chose to add an expense.")
    category = input("Please enter the category(Food, Travel, etc...): ")
    description = input("Pleaes enter a description of the expense: ")
    
    while True:
        try:
            amount = float(input("Please enter the amount of the expense: "))
            if amount <= 0:
                print("Amount must be a positive number. Please try again.")
            else:
                break
        except ValueError:
             print("Invalid input. Please enter a numerical value for the amount.")

    #Store the expense as a dictionary
    expense = {
        "category": category,
        "description": description,
        "amount": amount
    }

    #Add ecpense to expenses list
    expenses.append(expense)
    print("expense added successfully.\n")

def show_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
        
    print("=" * 40)
    print("Current Expenses:")
    print("=" * 40)
    
    total = 0  # 

    for expense in expenses:
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}")
        print(f"Amount: ${expense['amount']:.2f}")
        print("-" * 40)

# Add the amount to the total
        total += expense['amount']

    print(f"Total Expenses: ${total:.2f}")
    print("=" * 40)

def show_menu():

    print("=" * 60)
    print("Welcome to the expensy, the expense tracking program.")
    print("=" * 60)

    menu = """
    Please select an option:
    1. Add Expense
    2. View Expenses
    3. Filter
    4. Calculate Total
    5. Save and Quit
    """
    print(menu)


#Main program loop
while True:
    show_menu()
    choice = input("Enter your choice 1-5: ")

# Handling each choice
    if choice == "1":
        add_expense()

    elif choice == "2":
        print("You chose to view expenses")
        show_expenses()
         
    elif choice == "3":
        print("You chose to filter.")
        #Code for filtering

    elif choice == "4":
        print("You chose to calculate the total.")
        #Code for calculating the total.

    elif choice == "5":
        print("Saving and quitting...")
        #Code for saving and quitting.
        break #exit the loop

    else:
        print("Invalid choice, Please choose a valid option (1-5)")