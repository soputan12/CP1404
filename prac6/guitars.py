from guitar import Guitar

CURRENT_YEAR = 2021


def main():
    guitar_list = []
    print("My guitars!")
    name = input("Guitar: ")
    while name != "":
        year = check_year()
        cost = check_cost()
        guitar = Guitar(name, year, cost)
        guitar_list.append(guitar)
        print(f"{guitar} has been added to the list.")
        name = input("Guitar: ")
    #APPENDING FOR TEST
    guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitar_list:
        print("Guitar list:")
        for i, guitar in enumerate(guitar_list):
            vintage_guitars = ""
            if guitar.is_vintage():
                vintage_guitars = "Vintage"
            print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), Cost:${guitar.cost:10,.2f} {vintage_guitars}") #try to fix it until it looks right
    else:
        print("No Guitars.")
def check_year():
    year = int(input("Year: "))
    while year <= 0:
        print("Invalid")
        year = int(input("Year: "))
    else:
        return year

def check_cost():
    cost = float(input("Cost: "))
    while cost <= 0:
        print("Invalid")
        cost = float(input("Cost: "))
    else:
        return cost


main()