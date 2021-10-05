from datetime import date

class Student:

    def __init__(self, id, name, dob, classification):
        self.__studeentid = id
        self.__name = name
        self.__dob = dob
        self.__classification = classification
        self.__age = 0
        self.__register = ''

    #only need more objects after self if there is user input (only for mutator methods)
    #set methods need user input?
    def get_age(self):
        return self.__age

    def get_registration(self):
        return self.__register


    def register(self, classification):
        if classification == 'senior':
            self.__register = '11/1 thru 11/3'
        elif classification == 'junior':
             self.__register = '11/4 thru 11/6'
        elif classification == 'sophomore':
             self.__register = '11/7 thru 11/9'
        elif classification == 'freshman':
             self.__register = '11/10 thru 11/12'
        else:
            self._register = 'classification not found'

    def calc_age(self):
        today = date.today()
        bday = self.__dob.split('/')
        bday_year = int(bday[2])
        age = today.year - bday_year
        self.__age = age
    
            



