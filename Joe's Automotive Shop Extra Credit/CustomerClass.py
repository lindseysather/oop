class Customer:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone

class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def set_make(self, make):
        self.__make = make
    def set_model(self, model):
        self.__model = model
    def set_year(self, year):
        self.__year = year

    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year


class ServiceQuote:
    def __init__(self, pcharge, lcharge):
        self.__parts_charge = pcharge
        self.__labor_charge = lcharge
    
    def set_pcharge(self, pcharge):
        self.__parts_charge = pcharge
    def set_address(self, lcharge):
        self.__labor_charge = lcharge
 
    def get_pcharge(self):
        return self.__parts_charge
    def get_lcharge(self):
        return self.__labor_charge
 
    def get_sales_tax(self):
        tax_rate = 0.07
        self.__tax = float((self.__parts_charge + self.__labor_charge)*tax_rate)
        print('The sales tax is $' ,format(self.__tax, ',.2f'), sep='')

    def get_total_charges(self,tax):
        total = float(self.__parts_charge + self.__labor_charge + self.__tax)
        print('Total Charge: $', format(total, ',.2f'), sep='')