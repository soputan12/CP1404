import random
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():
    score = score = float(input("Enter score: "))
    #score = random.randint(0, 100)
    sorted_score = sort_score(score)
    print(f"Your score {score} has the grade {sort_score()}")

def sort_score(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        elif score < 50:
            return "Bad"

main()