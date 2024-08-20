# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("What is your savings account balance? "))
    savings_interest = float(input("What is the APR for the savings account? "))
    savings_maturity = int(input("How many months has your account been accruing interest? "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("APR Interest rate is: ",format(interest_earned, ", .2f"), "%")
    print("The balance is: $ ", format(savings_maturity), ", .2f")
    print("The updated savings account balance is:",format(savings_balance))

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("What is your CD balance?"))
    cd_interest = float(input("What is the APR for the cd?"))
    cd_maturity = int(input("How many months has your account been accruing interest?"))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(updated_cd_balance, interest_earned, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("APR Interest rate is: ",format(interest_earned, ", .2f"), "%")
    print("The balance is: $ ", format(cd_maturity), ", .2f")
    print("The updated cd account balance is:",format(cd_balance))

if __name__ == "__main__":
    # Call the main function.
    print(main)  