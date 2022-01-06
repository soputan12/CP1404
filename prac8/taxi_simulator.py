from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total = 0
    user_input = error_check()
    while user_input != "q":
        if user_input == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi = int(input("Choose taxi\n>>>"))
            try:
                current_taxi = taxis[taxi]
            except IndexError:
                print("Invalid")
        elif user_input == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input("How far\n>>>"))
                current_taxi.drive(distance)
                cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} cost you ${cost:.2f}")
                total += cost
        else:
            print("You need to choose a taxi before you can drive")
    else:
        print(f"Total bill: ${total:.2f}")
        print("Thank you!")


def error_check():
    user_input = input("q)uit, c)hoose taxi, d)rive\n>>>").lower()
    while user_input != "q" and user_input != "c" and user_input != "d":
        print("Invalid")
        user_input = input("q)uit, c)hoose taxi, d)rive\n>>>").lower()
    else:
        return user_input

def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
