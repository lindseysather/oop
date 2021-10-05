import CarClass as c

def main():

    year_model = input("Enter your car's year model: ")
    make = input("Enter your car's make: ")

    my_car = c.Car(year_model, make)

    print("\nYour", year_model, make, "is accelerating:")
    for count in range(5):
        my_car.accelerate()
        print("Current speed:", my_car.get_speed(), "mph")

    print("\nYour", year_model, make, "is braking:")
    for count in range(5):
        my_car.brake()
        print("Current speed:", my_car.get_speed(), "mph")

main()