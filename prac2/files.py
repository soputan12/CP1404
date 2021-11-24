name_file = open("name.txt", 'w')
name = input("What is your name? ")
print(name, file=name_file)
name_file.close()

name_file = open("name.txt", "r")
name = name_file.read()
print(f"Your name is {name}")
name_file.close()

number_file = open("numbers.txt", "r")
number1 = int(number_file.readline())
number2 = int(number_file.readline())
total = number1 + number2
print(total)
number_file.close()

number_file = open("numbers.txt", "r")
count = 0
for numbers in number_file:
    number = int(numbers)
    count += number
print(count)
number_file.close()