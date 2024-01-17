"""
Title: UWF Prescription Drug Service.
Author: Jon Burstein
Details: This is a python program to determine the cost of different insurance plans.
"""

b_final_cost = 0
s_final_cost = 0
d_final_cost = 0
print("Welcome to the UWF Prescription Drug Service")
print("Basic Plan B cost $10.00 monthly with $200.00 deductible and '40%' copay.")
print("Basic Plan S cost $30.00 monthly with $100.00 deductible and '20%' copay.")
print("Basic Plan D cost $75.00 monthly with $0.00 deductible and '0%' copay.")
choice = 'y'
while choice == "y" or choice == "yes":

    while True:
        plan = input("Which plan do you want?(B,S,D): ")
        plan = plan.upper()

        if plan in ['B','S','D']:
            break
        else:
            print(f"Plan {plan} is not an option, please enter only B, S, or D ")
    while True:
        num_prescription = input("How many prescriptions for the year?(1-96): ")
        num_prescription = int(num_prescription)

        if num_prescription > 0 and num_prescription < 97:
            break
        else:
            print(f"You entered an invalid unit of {num_prescription}, pleae enter a number between 1 and 96.")

    if plan == 'B':
        yearly_premium = 120
        deductible = 200
        total_prescription = 50 * num_prescription
        total_prescription = float(total_prescription)
        copay = (total_prescription - deductible) * .40
        b_final_cost = yearly_premium + copay + deductible
        print(f"Plan B will cost you ${round(b_final_cost,2)}")
        if b_final_cost > 0 and s_final_cost > 0:
            if b_final_cost > s_final_cost:
                savings = round(b_final_cost - s_final_cost,2)
                print(f"By switching to plan S, you will save ${savings}")
            elif s_final_cost > b_final_cost:
                savings = round(s_final_cost - b_final_cost,2)
                print(f"By switching to plan B, you will save ${savings}")
    elif plan == 'S':
        yearly_premium = 360
        deductible = 100
        total_prescription = 50 * num_prescription
        total_prescription = float(total_prescription)
        copay = (total_prescription - deductible) * .20
        s_final_cost = yearly_premium + copay + deductible
        print(f"${round(s_final_cost,2)}")
    elif plan == 'D':
        yearly_premium = 900
        total_prescription = 50 * num_prescription
        d_final_cost = yearly_premium 
        d_final_cost = float(d_final_cost)
        print(f"${round(d_final_cost,2)}")

    choice = input("Would you like to run the program again?: ")            
print("-------------------------------------------------------------")
print("Thank you for using the UWF Insurance App.")
print("Goodbye!!!")
print("-------------------------------------------------------------")