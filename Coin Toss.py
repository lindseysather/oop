
#CoinClass is the name of the file (importing entire file)
# Keep both files in the same file
# as c for easier typing 

import CoinClass as c


# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'
       # sets value to heads because we initialized it to heads in CoinClass

       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter
       # have to use instance not class -> my_coin not coin

       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss()
           
           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())

           


       

# Call the main function.

main()
