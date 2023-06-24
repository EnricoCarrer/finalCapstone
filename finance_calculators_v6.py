# CAPSTONE PROJECT I
# This program allows the user to access two financial calculators: an investment calculator and a home loan repayment calculator.
# Although not specifically requested for this task, I used difensive coding to handle invalid inputs.

# Firstly, import math module for a formula needed later
import math

# print instructions for the user and obtain first input (investment or bond)
print ("investment - to calculate the amount of interest you'll earn on your investment\nbond - to calculate the amount you'll have to pay on a home loan")

# use a while loop to handle spelling mistakes or other invalid inputs
while True: 
    user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower() 
    if user_choice in ['investment', 'bond']:
        break
    else: 
        print ("Unrecognised input. Please start again. ")

# Using the if statement and a try-excpet block to handle the input of non-numbers, ask the user to input necessary information in case the choice was "investment" 
if user_choice == "investment" : 
    while True: 
        try:
            deposit = float(input("Please enter the amount of money you want to deposit: £ ")) 
            i_rate = float(input("Please enter the interest rate as a percentage (e.g if the interest rate is 8%, please enter '8' without the sign '%'): ")) # input 3
            converted_i_rate = i_rate/100  # converting the percentage into decimal
            n_years = float(input("Please enter the number of years you plan on investing: "))  
            break
        except ValueError:
            print ("Invalid input. Try again.")

    # using an indented while loop, keep asking the user to chose the type of interest until a valid option is entered.
    while True:  
        interest = input ("Please choose the type of interest. Enter either 'simple' or 'compound': ").lower()  
        if interest in ['simple','compound']:
            break
        else:
            print ("Unrecognised input. Please start again. ")

    # using an if statement, calculate and print the final amount if the user enters "simple" interest
    if interest == "simple":
        final_amount = deposit * (1 + converted_i_rate * n_years)  # this is the formula for the simple interest
        rounded_final_amount = round(final_amount,2)    
        print(f"Your total amount at the end of the indicated timeframe will be: £ {rounded_final_amount}\nThank you for using this calculator.")
    
    # using an elif statement, calculate and print the final amount if the user enters "compound" interest
    elif interest == "compound":
        final_amount = deposit * math.pow((1+converted_i_rate),n_years)   # this is the formula for the compound interest
        rounded_final_amount = round(final_amount,2)
        print(f"Your total amount at the end of the indicated timeframe will be: £ {rounded_final_amount}\nThank you for using this calculator.")
            
# ask the user to input the necessary information in case the choice was "bond"
elif user_choice == "bond":
    
    # another while loop and try-except block to handle invalid inputs
    while True: 
        try:
            loan_value = int(input("Please enter the present value of the house (or the loan amount, e.g. 200000): £ "))    
            i_rate = float(input("Please enter the interest rate as a percentage (e.g if the interest rate is 4%, please enter '4' without the sign'%'): "))
            converted_i_rate = i_rate/100/12  # converting the yearly percentage into decimal and dividing by 12 to obtain the monthly rate
            n_years = int(input("Please enter the number of years you plan to take to repay the loan (e.g. 25 years): "))
            n_months = n_years*12
            # calculate and print the final amount
            monthly_repayment = (converted_i_rate * loan_value)/(1-(1+converted_i_rate)**(-n_months))   # this is the formula to calcualte the repayment
            rounded_monthly_repayment = round(monthly_repayment,2)
            print (f"The amount you will have to repay each month is: £ {rounded_monthly_repayment}\nThank you for using this calculator.") 
            break   
        except ValueError:
            print ("Invalid input. Try again.")
