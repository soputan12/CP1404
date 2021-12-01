number_list = []
for i in range(5):
    number = int(input("Number: "))
    number_list.append(number)
print(f"Your first number is {number_list[0]}")
print(f"Your last number is {number_list[-1]}")
print(f"Your smallest number is {min(number_list)}")
print(f"Your largest number is {max(number_list)}")
print(f"The average of the numbers is {sum(number_list) / len(number_list)}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_input = input("Username: ")
if user_input in usernames:
    print("Access Granted")
else:
    print("Access Denied")