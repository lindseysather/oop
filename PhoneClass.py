class Phone:

    def __init__(self, man, model, price):
        self.__manufact = man
        self.__model = model
        self.__retail_price = price

    def set_manufact(self, man):
       self.__manufact = man

    def set_model(self, model):
        self.__model = model
    
    def set_retail_price(self, price):
        self.__retail_price = price

    

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price   


    