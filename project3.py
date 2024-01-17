"""
Title: English to Metric Converter.
Author: Jon Burstein
Details: This is a python program that converts a few differnt measurements to their metric counterparts.
"""


def menu():
    while True:
        print("---English to Metric Converter---")
        print("1) Convert from feet (FT) to meters (m)")
        print("2) Convert from gallons (GAL) to liters (L)")
        print("3) Compute area of a rectangle in square meters given the length and width in Feet")
        print("4) Convert temperature from Fahrenheight (F) to Celsius (C)")
        print("5) Quit the Program.")
        choice = input("\nPlease enter a number (1-5) -> ")
        
        if choice == '1':
            feet = input("Please enter a value in feet -> ")
            feet = float(feet)
            print(f"{feet} is {format(feet_to_meter(feet),'.4f')} meters")
        elif choice == '2':
            print(f"{gallons_to_liters()} liters")
        elif choice =='3':
            print(area_of_rectangle())
        elif choice == '4':
            print(format(f_to_c(),'.2f'))
        elif choice == '5':
            print("-----------------")
            print("Goodbye!!!")
            print("-----------------")
            break

def feet_to_meter(feet):
    meters = feet * 0.3048
    return meters

def gallons_to_liters():
    gallons = input("Please enter a value in gallons -> ")
    gallons = float(gallons)
    liters = gallons * 3.78541
    return liters

def area_of_rectangle():
    length = input("Please enter a value for length -> ")
    length = float(length)
    width = input("Please enter a value for width -> ")
    width = float(width)
    area = length * width
    return area

def f_to_c():
    fah = input("Please enter a value for Fahrenheit -> ")
    fah = float(fah)
    cel = (fah - 32) * (5/9)
    return cel

menu()