from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total = 0
    user_input = error_check()
    while user_input != "q":
        if user_input == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi = taxi_check()
            try:
                current_taxi = taxis[taxi]
            except IndexError:
                print("Invalid taxi choice")
            print(f"Your Taxi is {current_taxi}")
        elif user_input == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input("How far do you want to drive? "))
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip costed you ${trip_cost:.2f}")
                total += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill: ${total:.2f}")
        user_input = error_check()

    print(f"Total trip cost: ${total:.2f}")
    print("Taxis are now: ")
    display_taxis(taxis)


def error_check():
    user_input = input("q)uit, c)hoose taxi, d)rive\n>>>").lower()
    while user_input != "q" and user_input != "c" and user_input != "d":
        print("Invalid")
        user_input = input("q)uit, c)hoose taxi, d)rive\n>>>").lower()
    else:
        return user_input


def taxi_check():
    taxi = int(input("Choose taxi: "))
    while 0 > taxi > 2:
        print("Invalid Number")
        taxi = int(input("Choose taxi: "))
    return taxi


def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
