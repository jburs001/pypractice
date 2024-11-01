#*****************************************************
# Author: Jon Burstein
# Assignment: A01
# Date: 01/31/2024
# Description: A program to convert Fahrenheit to Celcius
# Input: A float for the temperature in Fahrenheit
# Output: The float for the temperature in Celcius
# Source: 
#*****************************************************
def main():
    fahrenheit = 0.0
    celcius = 0.0

    print("***********Welcome to the PCC fahrenheit to celcius converter.**************")
    fahrenheit = input("\nPlease enter the temperature in fahrenheit you would like to convert to celcius: ")
    fahrenheit = float(fahrenheit)
    celcius = (fahrenheit - 32) * 5/9

    print('\n',fahrenheit, "degrees fahrenheit is", round(celcius,2), "degrees celcius.")
    print("\nThank you and have a great day!")

main()