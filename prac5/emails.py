def main():
    email_list = {}
    email = input("Email: ")
    while email != "":
        name = sort_email(email)
        confirm = input(f"Is your name {name}? (Y/N)")
        if confirm.lower() == "y" and confirm != "":
            email_list[email] = name
            email = input("Email: ")
        else:
            email = input("Please enter your Email again: ")
    for email, name in email_list.items():
        print(f"{name} ({email})")

def sort_email(email):
    pre_email = email.split('@')[0] #you split the wrong letter
    split_dot = pre_email.split('.')
    name = " ".join(split_dot).title()
    return name



main()