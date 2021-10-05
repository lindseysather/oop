import CustomerClass as c

def main():
    name = input("Name: ")
    address = input("Address: ")
    phone = input("Phone Number: ")

    make = input("Car Make: ")
    model = input("Car Model: ")
    year = int(input("Car Year: "))

    pcharge = float(input("Parts Charge: $"))
    lcharge = float(input("Labor Charge: $"))
    tax = 0.1


    new_customer = c.Customer(name, address, phone)
    customer_car = c.Car(make, model, year)
    customer_charges = c.ServiceQuote(pcharge, lcharge)


    print(f"\n{name}")
    print(address)
    print(phone)

    print(year, make, model)

    print('Parts Charge: $', format(pcharge, ',.2f'), sep='')
    print('Labor Charge: $', format(lcharge, ',.2f'), sep='')

    customer_charges.get_sales_tax()
    customer_charges.get_total_charges(tax)


main()



