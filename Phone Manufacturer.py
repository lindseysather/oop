

import PhoneClass

def main():
    

     man = input("Enter phone manufacturer:")
     model = input("Enter phone model: ")
     price = input("Enter phone price: $")

     phone = PhoneClass.Phone(man, model, price)

     print("Manufacturer:", man)
     print("Model:", model)
     print("Price:", price)


main()