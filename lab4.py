"""
Title: Cash register program
Author: Jon Burstein
Details: This is a python program to determine the tax of items entered by the user.
It teaches user input and if/else statements.
"""

user_input = input("Enter the number of items purchased: ")
num_items = int(user_input)
user_input = input("Enter the price per item: ")
price_per_item = float(user_input)
taxable = input("Is the purchase taxable? (y/n): ")
#total cost = number of items * pricer per item
#total_cost of all items plus 5.5% tax if taxable
untax_total = num_items * price_per_item
print(f"{num_items} items at ${price_per_item} each will cost ${round(untax_total,2)}")
#computer tax
tax = 5.5
total_tax = untax_total * (tax / 100)
final_bill = total_tax + untax_total

#Format to two decimal places
if taxable.lower() == 'y' or taxable.lower == "yes":
    print(f"Tax is ${round(total_tax,2)}")
    print(f"Final bill is ${round(final_bill,2)}")
else:
    print(f"Tax is $0.00")
    print(f"Final bill is: {round(untax_total,2)}")
