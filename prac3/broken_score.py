"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():
    score = float(input("Enter score: "))
    sorted_score = sort_score(score)
    print(sorted_score)

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