HEX_CODE = {"absolutezero": "#0048ba", "acidgreen": "#b0bf1a", "aliceblue": "#f0f8ff",
            "alizarincrimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00",
            "amethyst": "#9966cc", "antiquewhite": "#faebd7", "apricot": "#fbceb1",
            "aqua": "#00ffff"}
user_input = input("Colour: ")
while user_input != "":
    while user_input not in HEX_CODE:
        print("Invalid colour")
        user_input = input("Colour: ")
    print(f"The colour {user_input} has the code {HEX_CODE[user_input]}.")
    user_input = input("Colour: ")
else:
    print("Have a nice day!")
