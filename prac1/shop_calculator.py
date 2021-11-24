def main():
    number = get_number("Number of items:")
    count = number
    total = 0
    while count > 0:
        price = float(input("Price of item:"))
        total = total + price
        count -= 1
    else:
        discount = total * 0.1
        discounted_price = total - discount
        print(f"Total price for {number} items is ${discounted_price:.2f}")


def get_number(prompt):
    number = int(input(prompt))
    while number <= 0:
        print("Invalid number of items!")
        number = int(input(prompt))
    else:
        return number


main()
