"""
Title: Dresser Program
Author: Jon Burstein
Details: This is a python program that determines the cost of a dresser based on the type
of wood and number of drawers. It teaches functions 
"""

def get_drawers():
    while True:
        num_drawers = input("Enter the number of drawers in the desk: ")
        try:
            num_drawers = int(num_drawers)
            if 1 <= num_drawers <= 9:
             break
            else:
                print("The number must be between 1 and 9")
        except ValueError:
            print("try again.")
    return num_drawers
    
def get_wood():
    while True:
        wood_type = input("Enter wood type (m for mahogany, o for oak, or p for pine): ")
        wood_type = wood_type.lower()
        try:
            if wood_type == 'm' or wood_type == 'o' or wood_type == 'p':
                break
            else:
                print("Must be m, o, or p: try again")
        except ValueError:
             print("Must be 'm', 'o' or 'p': try again")
    return wood_type

def compute_price(drawers, wood):
    PINE = 115
    OAK = 170
    MAHOGANY = 225
    DRAWER = 23.50
    SHIPPING = 350
    price = 0.0

    if wood == 'p':
        price = format(PINE + (drawers * DRAWER) + SHIPPING,'.2f')
    if wood == 'o':
        price = format(OAK + (drawers * DRAWER) + SHIPPING,'.2f')
    if wood == 'm':
        price = format(MAHOGANY + (drawers * DRAWER) + SHIPPING,'.2f')
    
    return price

def display_price():
    drawers = get_drawers()
    wood = get_wood()
    total_price = compute_price(drawers,wood)

    print(f"Your total price for the desk with {drawers} drawers is ${total_price}")

choice = 'y'
while choice == 'y' or choice == 'yes':

    display_price()
    choice = input("Continue? Enter y for yes or any other character to quit: ")
    choice = choice.lower()

print("-----------------------")
print("Goodbye!!!")
print("-----------------------")