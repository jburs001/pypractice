"""
Title: File I/O
Author: Jon Burstein
Details: This is a python program that reads date from a text file and then parses that data
and organizes it into the number, the number squared, the sum of the numbers and product.
It teaches file input and output. 
"""

file_name = 'data.txt'
out_file = 'output.txt'

with open(file_name) as file_object:
    contents = file_object.readlines()
    digits = []
    for content in contents:
        # split each line into numbers (assuming they are space-separated)
        numbers = content.split()
        # add the numbers to the digits list
        digits.extend(numbers)
            
digits = [int(number) for number in digits]

even_digits = []
sum_of_digits = 0
product_of_digits = 1
average = 0


with open(out_file, 'w') as output_file:
    output_file.write("x      x^2      Current Sum      Product\n")
    output_file.write("===    ===      ===========      ========\n")
    for digit in digits:
        if digit % 2 == 0:
            even_digits.append(digit)
            sum_of_digits += digit
            product_of_digits *= digit
            average = sum_of_digits / len(even_digits)
            output_file.write(f"{digit:<7} {digit ** 2:<13} {sum_of_digits:<16} {product_of_digits}\n")
    output_file.write(f"The average of these even numbers is: {average}\n")   
