"""
Author: Jon Burstein
Details: This is a python program that determines the height of someones future children.
It teaches while loops, taking in user input, and if statements.
"""

import math

run_again = True

while run_again:
    print(f"Welcome to the UWF Child height determination program.")
    print("-----------------------------------------------------------")
    gender = input("Enter the gender of your future child. Use F for female or M for Male: ")
    gender = gender.upper()
    feet_mom,inches_mom = input("Enter the height in feet then the height in inches of the mom (separated by a space): ").split()
    feet_mom = int(feet_mom)
    inches_mom = int(inches_mom)
    total_inches_mom = (feet_mom * 12) + inches_mom

    feet_dad,inches_dad = input("Enter the height in feet then the height in inches of the dad (separated by a space): ").split()
    feet_dad = int(feet_dad)
    inches_dad = int(inches_dad)
    total_inches_dad = (feet_dad * 12) + inches_dad

    childHeightMale = ((total_inches_mom * 13/12) + total_inches_dad)/2
    childHeightFemale = ((total_inches_dad * 13/12) + total_inches_mom)/2

    if gender == "M":
        child_height_feet = round(childHeightMale // 12)
        child_height_inches = round(childHeightMale % 12)
        print(f"Your future child is estimated to grow to be {child_height_feet} {math.floor(child_height_inches)}.")

    if gender == "F":
        child_height_feet = round(childHeightFemale // 12)
        child_height_inches = round(childHeightFemale % 12)
        print(f"Your future child is estimated to grow to be {child_height_feet} {math.floor(child_height_inches)}.")
    choice = input("Enter r to return program any other character to exit: ")
    if choice.lower() != 'r':
        run_again = False