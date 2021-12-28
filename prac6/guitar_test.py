from guitar import Guitar
CURRENT_YEAR = 2021

def test():
    name = "Gibson L-5 CES"
    year = 1923
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2014, 1512.9)
    """ OUTPUT: 
        Gibson L-5 CES get_age() - Expected 98. Got 98
        Another Guitar get_age() - Expected 7. Got 7
        Gibson L-5 CES is_vintage() - Expected True. Got True
        Another Guitar is_vintage() - Expected False. Got False """

    print(f"{guitar.name} get_age() - Expected {98}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {7}. Got {other.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")

test()