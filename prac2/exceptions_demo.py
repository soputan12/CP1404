"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? ValueError occurs when a string or float is inputted instead of integers.
2. When will a ZeroDivisionError occur? ZeroDivisionError occurs when the denominator is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Tried multiple ways but try except is still the most efficient way.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
