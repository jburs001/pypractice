"""
Title: Improved Cash Register
Author: Jon Burstein
Details: This is an improvement on the previous lab it adds functionality 
like 0 tax and formatting to two decimal places.
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
    print(f"Final bill is ${round(final_bill,2)}\n")
    for item in range(1, num_items):
        print(f"For {item} item(s), tax is ${round((price_per_item * item) * (tax/100) ,2)} and final cost would be ${round(price_per_item * item  + (price_per_item * item) * (tax/100),2)}")
    print(f"Final bill for {num_items} item(s), tax is ${round(total_tax,2)} and final cost would be ${round(final_bill,2)}.")

else:
    print(f"Tax is $0.00")
    print(f"Final bill is: {round(untax_total,2)}")
    for item in range(1, num_items):
        print(f"For {item} item(s), tax is $0.00 and final cost would be ${round(price_per_item * item,2)}")
    print(f"Final bill for {item} item(s), tax is $0.00 and final cost would be ${round(untax_total,2)}")