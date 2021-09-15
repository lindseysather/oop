#This program demonstrates the BankAccount class.

import BankAccountClass

def main():
    
   # Get the starting balance.
   start_bal = float(input('Enter your starting balance: '))

   # Create a BankAccount object.
   #savings is the name of the bankaccount instance
   savings = BankAccountClass.BankAccount(start_bal)

   # Deposit the user's paycheck.
   pay = float(input('How much were you paid this week? '))
   print('I will deposit that into your account.')
   savings.deposit(pay)

   # Display the balance.
   print('Your account balance is $', format(savings.get_balance(), ',.2f'),
        sep='')

   # Get the amount to withdraw.
   cash = float(input('How much would you like to withdraw? '))
   print('I will withdraw that from your account.')
   savings.withdraw(cash)

   # Display the balance.
   print('Your account balance is $', 
        format(savings.get_balance(), ',.2f'),
        sep='')

   print(savings)


# Call the main function.
main()


#We don't trust the programmer making this. So we make our objects 
# in our own thing with hidden attributes and if/else stuff