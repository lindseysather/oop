import CarClass as c

def main():

    year_model = int(input("Enter your car's year model: "))
    make = input("Enter your car's make: ")

    my_car = c.Car(year_model, make)

    for count in range(5):
        my_car.accelerate()
        print("Current speed:", my_car.get_speed(), "mph")

    for count in range(5):
        my_car.brake()
        print("Current speed:", my_car.get_speed(), "mph")

main()