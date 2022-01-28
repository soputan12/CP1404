"""
CP1404/CP5632 Practical
Recursion
"""


# def do_it(n):
#     """Do... it."""
#     if n <= 0:
#         return 0
#     return n % 2 + do_it(n - 1)
#
#
# # It will 1st check whether n is less than or = to 0 n den return n % 2 + do_it(n - 1) and then cycle it back over n over until it reaches 0
# print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        print(n ** 2)
    return do_something(n - 1)

# it will multiply it ** 2 if n is less than 0 and then reduce n by 1 n repeat until its more than 0
do_something(4)

