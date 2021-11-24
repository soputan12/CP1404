MIN_LENGTH = 2

def main():
    password = get_password(MIN_LENGTH)
    print_asterisk(password)




def get_password(MIN_LENGTH):
    password = input(f"Password(Minimum Length {MIN_LENGTH}): ")
    while len(password) < MIN_LENGTH:
        print("Invalid Length")
        password = input(f"Password(Minimum Length {MIN_LENGTH}: ")
    else:
        return password


def print_asterisk(password):
    print("*" * len(password))



main()



